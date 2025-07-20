from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# Read the API key
api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10,openai_api_key=api_key)

result = model.invoke("Why person should learn data science?")

print(result.content)