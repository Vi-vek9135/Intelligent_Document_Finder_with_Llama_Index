# from To_Fetch_Multiples_documents_from_drive import load_data
# from llama_index.core import VectorStoreIndex
# from llama_index.llms.openai import OpenAI
# import streamlit as st
# from llama_index.llms.openai import OpenAI
# from dotenv import load_dotenv
# import openai
# import os

# load_dotenv()  # Load the .env file

# openai.api_key = os.getenv('OPENAI_API_KEY')


# # Model I am using is gpt-3.5-turbo
# llm = OpenAI(temperature=0, model="gpt-3.5-turbo")



# # This function is for importing the documents by fetching the documents from the drive.
# @st.cache_resource(show_spinner=False)
# def import_docs_by_fetching_documents_from_drive():
#     with st.spinner(text="Loading and indexing your docs – hang tight! This should take 1-2 minutes."):
#         docs = load_data(folder_id="1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL")
#         index = VectorStoreIndex.from_documents(docs)
#     return index



# # This is for automating the data storage and indexing.  




















import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.llms.openai import OpenAI
import openai




import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

openai.api_key = os.getenv('OPENAI_API_KEY')  # Get the API key

# print(api_key)  # Print the API key


# load some documents
documents = SimpleDirectoryReader("./data").load_data()

# initialize client, setting path to save data
db = chromadb.PersistentClient(path="./chroma_db")

# create collection
chroma_collection = db.get_or_create_collection("quickstart")

# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# create your index
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

# create a query engine and query
query_engine = index.as_query_engine()
response = query_engine.query("What is Section 138?")
print(response)




# This is for the data storage and indexing by using the chroma db.
