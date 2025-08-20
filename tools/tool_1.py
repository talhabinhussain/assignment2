from agents import function_tool,RunContextWrapper,FunctionTool
from my_schema.pydantic_schema import Subtraction



@function_tool(name_override="subtract_tool",description_override="subtract two numbers") # this is decorator function tool for  making tool just add decorator at the top of the function but it not  use the Pydantic schema for context validation — unless you manually implement it or use a FunctionTool with params_json_schema.
def subtraction_1(n1:int,n2:int):
    """subtract two numbers"""
    return f" after subtraction of {n1} and {n2}  = {n1-n2} "


async def subtraction_2(ctx:RunContextWrapper[Subtraction],args): # this is custom tool and it works with Pydantic schema for context validation 
    print("subtract tool call...")
    obj = Subtraction.model_validate_json(args)
    return f" after subtracting {obj.number1} and {obj.number2} is  = {obj.number1 - obj.number2}"



subtract_tool = FunctionTool(
    name="subtract_tool",
    description="Subtract two numbers",
    params_json_schema=Subtraction.model_json_schema(),
    on_invoke_tool=subtraction_2
)



