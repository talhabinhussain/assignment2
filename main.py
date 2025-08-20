from agents import Runner,RunConfig,SQLiteSession
from openai.types.responses import ResponseTextDeltaEvent
from my_config.gemini_config import Model,external_client
from my_agents.math_agent import math_agent
from my_schema.pydantic_schema import Subtraction
from my_agents.triage_agent import triage_agent
import asyncio



config = RunConfig(model=Model,model_provider=external_client,tracing_disabled=True)


# result = Runner.run_sync(triage_agent,prompt,run_config=config,context=Subtraction)



async def main():
    prompt = input("Enter your question: ")

    my_session = SQLiteSession('session_id_123',"conversation.db")
    result = Runner.run_streamed(triage_agent,prompt,run_config=config,context=Subtraction,session=my_session)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent):
            print(event.data.delta)
            
    #-----------------------------------------------------        

    prompt = input("Enter your question: ")

    my_session = SQLiteSession('session_id_123',"conversation.db")
    result = Runner.run_streamed(triage_agent,prompt,run_config=config,context=Subtraction,session=my_session)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent):
            print(event.data.delta)

    #-----------------------------------------------------        
    prompt = input("Enter your question: ")

    my_session = SQLiteSession('session_id_123',"conversation.db")
    result = Runner.run_streamed(triage_agent,prompt,run_config=config,context=Subtraction,session=my_session)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent):
            print(event.data.delta)





asyncio.run(main())

