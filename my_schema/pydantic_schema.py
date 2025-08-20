from pydantic import BaseModel


class Subtraction(BaseModel):
    number1:int
    number2:int


# while dataclasses and pydantic both are used for data handling and defining data structures in python dataclasses are builtin python module focus to reducing boilerplate code and generate method like '__init__' ,'__repr__' and '__eq__' pydantic on the other hand  pydantic is the third party library that emphasize data validation and offering more robust  type checking  