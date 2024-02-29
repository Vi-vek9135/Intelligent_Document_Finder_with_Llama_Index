# Importing the index from the Automate_Data_Storage_and_Indexing.py file

from Automate_Data_Storage_and_Indexing import import_docs_by_fetching_documents_from_drive 
from llama_index.llms.openai import OpenAI
# from To_Fetch_Metadata_Of_File import metadata


# Importing the streamlit as st and load_dotenv from dotenv
import streamlit as st
from dotenv import load_dotenv
import openai
import os


# Load the .env file
load_dotenv() 

openai.api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0, model="gpt-3.5-turbo")




st.set_page_config(page_title="Intelligent Document Finder with Llama Index", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
# openai.api_key = st.secrets.openai_key
st.title("Chat with the your documents, powered by LlamaIndex 💬🦙")

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about your documents's content!"},
    ]


index = import_docs_by_fetching_documents_from_drive()


if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history

            # def reutrn_response():
            #     return response.response
            # metadata()

            for node in response.source_nodes:
                st.write("-----")
                text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
                st.write(f"Text:\t {text_fmt} ...")
                st.write(f"Metadata:\t {node.node.metadata}")
                st.write(f"Score:\t {node.score:.3f}")

           






















# # Importing the index from the Automate_Data_Storage_and_Indexing.py file

# from Automate_Data_Storage_and_Indexing import import_docs_by_fetching_documents_from_drive 
# from llama_index.llms.openai import OpenAI

# # Importing the streamlit as st and load_dotenv from dotenv
# import streamlit as st
# from dotenv import load_dotenv
# import openai
# import os


# # Load the .env file
# load_dotenv() 

# openai.api_key = os.getenv('OPENAI_API_KEY')

# llm = OpenAI(temperature=0, model="gpt-3.5-turbo")

# # Set page configuration
# st.set_page_config(page_title="Intelligent Document Finder with Llama Index", page_icon="🦙", layout="wide")

# # Title and sidebar
# st.title("Chat with your documents, powered by LlamaIndex 💬🦙")
# with st.sidebar:
#     st.subheader("Options")
#     chat_mode = st.selectbox("Chat Mode", ["condense_question", "other_mode"])
#     temperature = st.slider("Temperature", 0.0, 1.0, 0.5)

# # Initialize chat history and engine
# if "messages" not in st.session_state.keys():
#     st.session_state.messages = [{"role": "assistant", "content": "Ask me a question about your documents' content!"}]

# index = import_docs_by_fetching_documents_from_drive()

# if "chat_engine" not in st.session_state.keys():
#     st.session_state.chat_engine = index.as_chat_engine(chat_mode=chat_mode, verbose=True, temperature=temperature)

# # User input and display messages
# if prompt := st.chat_input("Your question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# # Generate assistant response
# if st.session_state.messages[-1]["role"] != "assistant":
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response = st.session_state.chat_engine.chat(prompt)
#             st.write(response.response)
#             message = {"role": "assistant", "content": response.response}
#             st.session_state.messages.append(message)

#             # Display source nodes
#             for node in response.source_nodes:
#                 st.write("-----")
#                 text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
#                 st.write(f"Text: {text_fmt} ...")
#                 st.write(f"Metadata: {node.node.metadata}")
#                 st.write(f"Score: {node.score:.3f}")
