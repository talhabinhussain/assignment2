from agents import AsyncOpenAI ,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os


load_dotenv(override=True)

api_key = os.environ.get("GEMINI_API_KEY")
base_url = os.environ.get("BASE_URL")
gemini_model = os.environ.get("AI_MODEL")



external_client = AsyncOpenAI(api_key=api_key,base_url=base_url)


Model = OpenAIChatCompletionsModel(openai_client=external_client,model=gemini_model)


