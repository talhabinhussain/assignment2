from agents import Agent
from tools.tool_1 import subtract_tool

math_agent = Agent(name="Math Agent",
   instructions="""  You are a math agent. When the user asks to subtract two numbers, 
        use the 'subtract_tool' function tool to do it.
        Input numbers as 'n1' and 'n2'""",
   tools=[subtract_tool]
     )
