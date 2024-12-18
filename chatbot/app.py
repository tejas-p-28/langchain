from langchain_openai import ChatOpenAI # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore

import streamlit as st # type: ignore
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","please respond to the queries"),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title("Langchain Demo with OPENAI API")
input_text=st.text_input("Search topic you want to know")


#openai llm 
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))