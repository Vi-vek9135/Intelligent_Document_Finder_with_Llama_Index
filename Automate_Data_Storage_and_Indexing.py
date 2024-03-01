# Importing necessary modules for data loading and indexing
from To_Fetch_Multiples_documents_from_drive import load_data
from llama_index.core import VectorStoreIndex


import streamlit as st
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import openai
import os


# Load environment variables from the .env file
load_dotenv()  


# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')


# Initialize the LLM with the specified model and temperature
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")



# Define a function to import documents by fetching them from Google Drive
# The function is cached to avoid reloading and reindexing documents on every call
@st.cache_resource(show_spinner=False)
def import_docs_by_fetching_documents_from_drive():

    # Display a spinner in the Streamlit app to indicate that documents are being loaded and indexed
    with st.spinner(text="Loading and indexing your docs – hang tight! This should take 1-2 minutes."):

        # Load documents from the specified Google Drive folder ID
        docs = load_data(folder_id="1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL")
        # docs = load_data(folder_id="18amwk7k6u8Tlr02IQGRYnlrsGEWsNnnA")

        # Create a VectorStoreIndex from the loaded documents for efficient searching
        index = VectorStoreIndex.from_documents(docs)
    return index



# This is for automating the data storage and indexing.  

















