#import libraries for creating environment
import os
from dotenv import load_dotenv
load_dotenv()

#creating environment
os.environ['langchain_api_key']=os.getenv('langchain_api_key')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ["LANGCHAIN_PROJECT"]='Basic Generative AI App'

#import libraries for making app
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#build model
llm=Ollama(model='gemma:2b')
prompt=ChatPromptTemplate([
    ("system",'You are a helpful assistant.'),
    ('user',"Qustion: {question}")]
)
parser=StrOutputParser()
chain=prompt|llm|parser

#design streamlit app
st.title('Dream')
chat=st.text_input('Ask what is in your mind')
button=st.button('Generate')
if button:
    if chat:
        st.write(chain.invoke({'question':chat}))
    else:
        st.write('Please ask what is in your mind')