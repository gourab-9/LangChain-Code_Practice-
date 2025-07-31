from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')


prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(api_key = api_key)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'Career in Data Science'})

print(result)

chain.get_graph().print_ascii()