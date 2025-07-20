import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

# Load environment variables from .env (override any existing ones)
load_dotenv(override=True)

# Read the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the LLM
llm = OpenAI(model='gpt-3.5-turbo-instruct', openai_api_key=api_key)

# Invoke a test prompt
result = llm.invoke("What is the capital of India")

# Print result
print(result)
