# Importing the index from the Automate_Data_Storage_and_Indexing.py file and the OpenAI class from llama_index.llms.openai

from Automate_Data_Storage_and_Indexing import import_docs_by_fetching_documents_from_drive 
from llama_index.llms.openai import OpenAI
# from To_Fetch_Metadata_Of_File import metadata  (For testing purpose)
import requests



# Importing Streamlit for UI and dotenv for loading environment variable from the .env file
import streamlit as st
from dotenv import load_dotenv
import openai
import os

from From_Drive_Link import returnfolder_id


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





# Function to perform document search and display the results

def perform_document_search(prompt, chat_engine):
    with st.spinner("Thinking..."):
        response = chat_engine.chat(prompt)
        st.write(response.response)

        for node in response.source_nodes:
            st.write("-----")
            text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
            st.write(f"Text:\t {text_fmt} ...")
            st.write(f"Metadata:\t {node.node.metadata}")
            st.write(f"Score:\t {node.score:.3f}")
            st.write("-----")







# # This function sends a POST request to the backend API to register a new user
def register_user(username, email, password):
    data = {"username": username, "email": email, "password": password}
    response = requests.post("http://localhost:8000/register", json=data)
    if response.status_code == 200:
        # return response.json()
        # If the registration is successful, check for the access_token in the response
        response_data = response.json()
        if "access_token" in response_data:
            return response_data
        else:
            return {"error": "Registration successful, but access token not received"}
    else:
        return {"error": response.json().get("detail", "Registration failed")}



# # This function sends a POST request to the backend API to log in a user
def login_user(email, password):
    data = {"email": email, "password": password}
    response = requests.post("http://localhost:8000/login", json=data)
    return response.json()




# This function logs out the user by removing the access token from the session state
def logout():
    # Handle logout functionality if needed
    st.session_state.pop("access_token", None)
    st.write("You have been logged out.")








# The main function where the Streamlit app logic resides
def main():
    st.title("Intelligent Document Finder with Llama Index")



    # # Create buttons for registration, login, and logout
    button_clicked = st.sidebar.radio("", ["Register", "Login", "Logout"])


    # If the "Register" button is clicked, show the registration form
    if button_clicked == "Register":
        with st.form("register"):
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Register")
            if submitted:
                response = register_user(username, email, password)
                # if "message" in response:
                #     st.write(response["message"])
                # else:
                #     st.write("Registration failed")
                if "access_token" in response:
                    st.session_state["access_token"] = response["access_token"]
                    st.write("Registration successful! You are now logged in.")
                elif "error" in response:
                    st.write(response["error"])








    # # If the "Login" button is clicked, show the login form
    elif button_clicked == "Login":
        with st.form("login"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                response = login_user(email, password)
                if "access_token" in response:
                    st.session_state["access_token"] = response["access_token"]
                    st.write("Login successful!")
                else:
                    st.write(response.get("detail", "Login failed"))


    # If the "Logout" button is clicked, log out the user
    elif button_clicked == "Logout":
        logout()





    

    

    
    # If the user is logged in (access_token is in the session state)
    if "access_token" in st.session_state:
        st.title("Document Search")

        # Get the folder ID from Google Drive link
        folder_id = returnfolder_id()
        if folder_id is not None:
            # Import the document index by fetching documents from Google Drive
            index = import_docs_by_fetching_documents_from_drive(folder_id)


            # Initialize the chat engine if it doesn't exist in the session state
            if "chat_engine" not in st.session_state.keys():
                st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

            # Prompt for user input and save it to the chat history
            if prompt := st.chat_input("Your question"):
                st.session_state.messages.append({"role": "user", "content": prompt})

            # Display the prior chat messages
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])

            # If the last message is not from the assistant, generate a new response
            if st.session_state.messages[-1]["role"] != "assistant":
                with st.chat_message("assistant"):
                    perform_document_search(prompt, st.session_state.chat_engine)
    


    # If the "Logout" button is clicked, log out the user
    if st.button("Logout"):
        st.session_state.clear()
        st.write("Logout successful!")




# Start the Streamlit app
if __name__ == "__main__":
    main()





