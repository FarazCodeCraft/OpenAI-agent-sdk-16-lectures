# def main():
#     print("Hello from practice!")


# if __name__ == "__main__":
#     main()
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# import os
# from dotenv import load_dotenv
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     )
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
#     name="funny agent",
#     instructions="An agent that is funny and can answer questions with humor.",
# )
# result = Runner.run_sync(
#     agent,
#     input="What is the best way to make an ai agent  from scratch",
#     run_config=config,
# )
# print(result.final_output) 
# Should print a humorous response about making an AI agent from scratch






#handoffs
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# import os
# from dotenv import load_dotenv
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     )
# model = OpenAIChatCompletionsModel(
#     openai_client=external_client,
#     model="gemini-2.0-flash",
# )
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True,
# )
# history_tutor_agent = Agent(
#     name="History Tutor",
#     handoff_description="Specialist agent for historical questions",
#     instructions="You provide assistance with historical queries. Explain important events and context clearly.",
# )

# math_tutor_agent = Agent(
#     name="Math Tutor",
#     handoff_description="Specialist agent for math questions",
#     instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
# )

# agent = Agent(
#     name="web devdeloper",
#     handoffs=[history_tutor_agent, math_tutor_agent],
#     instructions="An agent that answer web development related queries and can hand off to specialized agents for history and math questions.",
# )
# result = Runner.run_sync(
#     agent,
#     input="tell me about world war 2",
#     run_config=config,
# )
# print(result.final_output)
# print(result)




#guardrails
# from dotenv import load_dotenv
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     )
# model = OpenAIChatCompletionsModel(
#     openai_client=external_client,
#     model="gemini-2.0-flash",
# )
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True,
# )



 



# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# from pydantic import BaseModel 
# import os
# from dotenv import load_dotenv
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# class CalendarEvent(BaseModel):
#     name: str
#     date: str
#     participants: list[str]
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     )
# model = OpenAIChatCompletionsModel(
#     openai_client=external_client,
#     model="gemini-2.0-flash",
# )
# config = RunConfig(
# #     model=model,
# #     model_provider=external_client,
# #     tracing_disabled=True,
# # )
# # history_tutor_agent = Agent(
# #     name="History Tutor",
# #     handoff_description="Specialist agent for historical questions",
# #     instructions="You provide assistance with historical queries. Explain important events and context clearly.",
# # )

# # math_tutor_agent = Agent(
# #     name="Math Tutor",
# #     handoff_description="Specialist agent for math questions",
# #     instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
# # )

# # agent = Agent(
# #     name="assistant",
# #     # handoffs=[history_tutor_agent, math_tutor_agent],
# #     instructions="An agent that extract calendar information from text",
# #     output_type = CalendarEvent,
# # )
# # result = Runner.run_sync(
# #     agent,
# #     input="tell me about the meeting with John on 2023-10-15 at 10:00 AM",
# #     run_config=config,
# # )
# # # print(result.final_output)
# # print(result)


# # from dataclasses import dataclass
# # class Car():
# #     def __init__(self, make, model, year):
# #         self.make = make
# #         self.model = model
# #         self.year = year
# #         print("this is my constuctor method")

# #     def start(self):
# #         return f"{self.year} {self.make} {self.model} is starting."

# #     def stop(self):
# #         return f"{self.year} {self.make} {self.model} is stopping."

# # new_car = Car("Toyota", "Corolla", 2030)
# # print(new_car.start())
# # print(new_car.stop())



# from dataclasses import dataclass
# @dataclass
# class Car:
#     make: str
#     model: str
#     year: int
#     print("this is my dataclass method")

#     def start(self):
#         return f"{self.year} {self.make} {self.model} is starting."

#     def stop(self):
#         return f"{self.year} {self.make} {self.model} is stopping."
    
# new_car = Car("Toyota", "Corolla", 2030)
# # print(new_car.start())
# print(new_car)
    




# # context = context_Class("name"=faraz, "age"=20)
# # context = ctx.context
# # ctx = context



# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# import os
# from dotenv import load_dotenv
# from dataclasses import dataclass
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# @dataclass
# class UserContext:
#     uid: str
#     is_pro_user: bool

# context_data = UserContext(
#     uid="12345",
#     is_pro_user=True
# )   

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#     )
# model = OpenAIChatCompletionsModel(
#     openai_client=external_client,
#     model="gemini-2.0-flash",
# )
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True,
# )
# history_tutor_agent = Agent(
#     name="History Tutor",
#     handoff_description="Specialist agent for historical questions",
#     instructions="You provide assistance with historical queries. Explain important events and context clearly.",
# )

# math_tutor_agent = Agent(
#     name="Math Tutor",
#     handoff_description="Specialist agent for math questions",
#     instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
# )

# agent = Agent(
#     name="web devdeloper",
#     handoffs=[history_tutor_agent, math_tutor_agent],
#     instructions="An agent that answer web development related queries and can hand off to specialized agents for history and math questions.",
# )
# result = Runner.run_sync(
#     agent,
#     input="tell me about world war 2",
#     run_config=config,
#     context=context_data
# )
# print(result.final_output)
# print(result)





# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# import os
# from dotenv import load_dotenv
# from dataclasses import dataclass
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
#full intro print
from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from dataclasses import dataclass
import asyncio

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")



@dataclass
class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str
    answer: str
@dataclass
class UserContext:
    uid: str
    is_pro_user: bool

context_data = UserContext(
    uid="12345",
    is_pro_user=True
) 





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
guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)


async def homework_guardrail(our_context, agent, input_data):
    result = await Runner.run(guardrail_agent, input="what is homework?", context=our_context, run_config=config)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    # input_guardrails=[
    #     InputGuardrail(guardrail_function=homework_guardrail),
    # ],
)

async def main():
    # result = await Runner.run(triage_agent, "who was the first president of the united states?", run_config=config, context=context_data)
    # print(result.final_output)

    # result = await Runner.run(triage_agent, "what is life?", run_config=config, context=context_data)
    # print(result.final_output)
    print(await homework_guardrail(context_data, guardrail_agent, "what is homework?"))


