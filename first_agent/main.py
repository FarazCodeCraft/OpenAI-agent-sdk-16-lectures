# def main():
#     print("Hello from first-agent!")


# if __name__ == "__main__":
#     main()
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import os
from dotenv import load_dotenv
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
    name="tech_expert",
    instructions="An agent that is tech_expert and can answer questions about technology trends wisely.",
)
result = Runner.run_sync(
    agent,
    input="What will be  the best field in 2030?, ai,ml,se,data science,web development, and also tell why",
    run_config=config,  
)
print(result.final_output)  # Should print "Paris"

