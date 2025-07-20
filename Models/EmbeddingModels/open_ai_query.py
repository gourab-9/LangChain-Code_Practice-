from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32,
    api_key=api_key   
)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))
