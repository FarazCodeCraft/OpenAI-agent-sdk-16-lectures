from agents import Agent, Runner, RunConfig,OpenAIChatCompletionsModel, AsyncOpenAI
import os
from dotenv import load_dotenv      
import chainlit as cl
import asyncio
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
external_client = AsyncOpenAI( 
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel( 
    openai_client=external_client,
    model="gemini-2.0-flash",
)   
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)   
agent = Agent(
    name="cook_expert",
    instructions="An agent that is cook_expert and can answer questions about cooking wisely.",
)
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content="Welcome to the cooking expert agent! How can I assist you today?"
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history") or []  # Use empty list if history is None.
    history.append({"role": "user", "content": message.content})
    result = await Runner.run(
        agent,
        input=history,
        run_config=config
    )
    history.append({"role": "system", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()
# @cl.on_message
# async def handle_message(message: cl.Message):
#     try:
#         history = cl.user_session.get("history") or []
#         history.append({"role": "user", "content": message.content})

#         result = await Runner.run(agent, input=message.content, run_config=config)
#         history.append({"role": "system", "content": result.final_output})

#         cl.user_session.set("history", history)
#         await cl.Message(content=result.final_output).send()
#     except Exception as e:
#         print("🔥 Error in handle_message:", e)
#         # Also send a user‑friendly error back so you know it failed:
#         await cl.Message(content="Sorry—I hit an error!").send()



