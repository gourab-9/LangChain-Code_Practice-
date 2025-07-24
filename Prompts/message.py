from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv(override=True)


# Read the API key
api_key = os.getenv("OPENAI_API_KEY")


model = ChatOpenAI(openai_api_key=api_key, temperature=1.5)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about SQL and Pandas')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

