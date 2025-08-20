from agents import Agent,handoff,RunContextWrapper
from my_agents.math_agent import  math_agent
from agents.extensions import handoff_filters
from my_agents.assistant_agent import assistant_agent
from my_schema.pydantic_schema import Subtraction


def math_handoff_fun(ctx:RunContextWrapper[Subtraction],input_data:Subtraction):
    print("math agent is calling... ")
    print(f'Subtract number {input_data.number1} and {input_data.number2}')


def assistant_handoff_fun(ctx:RunContextWrapper):
    print("assistant agent is calling... ")


math_handoff = handoff(
    agent=math_agent,
    tool_name_override="math_handoff_agent",
    tool_description_override="calling tool for calculation",
    on_handoff=math_handoff_fun,
    input_type=Subtraction,
    input_filter=handoff_filters.remove_all_tools
)

assistant_handoff = handoff(
    agent=assistant_agent,
    tool_name_override="general_assistant_handoff",
    tool_description_override="Answer the user prompt",
    on_handoff=assistant_handoff_fun,
    input_filter=handoff_filters.remove_all_tools
)

triage_agent = Agent(name="Triage Agent",
   instructions=""" You are able to do delegate task to the best and suitable agent """,
   handoffs=[math_handoff,assistant_handoff],
  
     )