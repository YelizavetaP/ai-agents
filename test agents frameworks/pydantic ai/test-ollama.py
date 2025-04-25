from pydantic_ai import Agent
# from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.ollama import OllamaModel
import os
from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")


model = OpenAIModel("gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

agent = Agent(model=model)

res = agent.run_sync("What is the capital of Italy?").data

print(res)

