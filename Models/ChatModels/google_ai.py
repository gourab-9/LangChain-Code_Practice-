from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv(override=True)

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',google_api_key=api_key)

result = model.invoke('What is the capital of India')

print(result.content)