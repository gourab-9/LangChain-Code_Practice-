from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv(override=True)


# Read the API key
api_key = os.getenv("OPENAI_API_KEY")


model = ChatOpenAI(openai_api_key=api_key, temperature=1.5)

# detailed way
template2 = PromptTemplate(
    template='Greet this person in 5 Indian languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'Gourab Singh'})

result = model.invoke(prompt)

print(result.content)

