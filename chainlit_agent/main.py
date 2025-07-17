# # def main():
# #     print("Hello from chainlit-agent!")


# # if __name__ == "__main__":
#     main()
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# import chainlit as cl
# import os
# from dotenv import load_dotenv
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )
# model = OpenAIChatCompletionsModel(
#     openai_client=external_client,
#     model="gemini-2.0-flash",
# )
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True,
# )
# agent = Agent(
#     name="cook_expert",
#     instructions="An agent that is cook_expert and can answer questions about cooking wisely.",
# )
# # result = Runner.run_sync(
# #     agent,
# #     input="Hello how are you?",
# #     run_config=config
# # )
# # print(result.final_output)

# @cl.on_message
# async def handle_message(message: cl.Message):
#     result = await Runner.run(
#         agent,
#         input=message.content,
#         run_config=config
#     )
#     await cl.Message(content=result.final_output).send()

import chainlit as cl


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"The user sends that : {message.content}",
    ).send()
@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Morning routine ideation",
            message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
            icon="/public/idea.svg",
            ),

        cl.Starter(
            label="Explain superconductors",
            message="Explain superconductors like I'm five years old.",
            icon="/public/learn.svg",
            ),
        cl.Starter(
            label="Python script for daily email reports",
            message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
            icon="/public/terminal.svg",
            ),
        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
            icon="/public/write.svg",
            )
        ]
 

# @cl.set_chat_profiles
# async def chat_profile(current_user: cl.User):
#     if current_user.metadata["role"] != "ADMIN":
#         return None

#     return [
#         cl.ChatProfile(
#             name="My Chat Profile",
#             icon="https://picsum.photos/250",
#             markdown_description="The underlying LLM model is **GPT-3.5**, a *175B parameter model* trained on 410GB of text data.",
#             starters=[
#                 cl.Starter(
#                     label="Morning routine ideation",
#                     message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
#                     icon="/public/idea.svg",
#                 ),
#                 cl.Starter(
#                     label="Explain superconductors",
#                     message="Explain superconductors like I'm five years old.",
#                     icon="/public/learn.svg",
#                 ),
#             ],
#         )
#     ]
