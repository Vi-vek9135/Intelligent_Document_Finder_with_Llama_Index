from To_Fetch_Multiples_documents_from_drive import load_data
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
import streamlit as st
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import openai
import os

load_dotenv()  # Load the .env file

openai.api_key = os.getenv('OPENAI_API_KEY')


# Model I am using is gpt-3.5-turbo
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")



# This function is for importing the documents by fetching the documents from the drive.
@st.cache_resource(show_spinner=False)
def import_docs_by_fetching_documents_from_drive():
    with st.spinner(text="Loading and indexing your docs – hang tight! This should take 1-2 minutes."):
        docs = load_data(folder_id="1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL")
        index = VectorStoreIndex.from_documents(docs)
    return index



# This is for automating the data storage and indexing.  





















