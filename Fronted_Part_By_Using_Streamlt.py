# Importing the index from the Automate_Data_Storage_and_Indexing.py file and the OpenAI class from llama_index.llms.openai

from Automate_Data_Storage_and_Indexing import import_docs_by_fetching_documents_from_drive 
from llama_index.llms.openai import OpenAI
# from To_Fetch_Metadata_Of_File import metadata



# Importing Streamlit for UI and dotenv for loading environment variable from the .env file
import streamlit as st
from dotenv import load_dotenv
import openai
import os


# Load environment variables from the .env file
load_dotenv() 

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')


# Initialize the LLM with specific parameters
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")



# Configure Streamlit page settings
st.set_page_config(page_title="Intelligent Document Finder with Llama Index", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Chat with the your documents, powered by LlamaIndex 💬🦙")


# Initialize the chat messages history if not already present in session state
if "messages" not in st.session_state.keys(): 
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about your documents's content!"},
    ]



# Import the document index by fetching documents from a drive
index = import_docs_by_fetching_documents_from_drive()


# Initialize the chat engine if not already present in session state
if "chat_engine" not in st.session_state.keys(): 
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)


# Prompt for user input and save to chat history
if prompt := st.chat_input("Your question"): 
    st.session_state.messages.append({"role": "user", "content": prompt})


# Display the prior chat messages
for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])



# If the last message is not from the assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            # Generate a response from the chat engine
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)

            # Add the assistant's response to the message history
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) 

        


            # Display the source nodes that contributed to the response
            for node in response.source_nodes:
                st.write("-----")

                # Format and display a snippet of the text from the source node
                text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
                st.write(f"Text:\t {text_fmt} ...")

                # Display metadata associated with the source node
                st.write(f"Metadata:\t {node.node.metadata}")

                # Display the score of the source node
                st.write(f"Score:\t {node.score:.3f}")

                st.write("-----")

           

