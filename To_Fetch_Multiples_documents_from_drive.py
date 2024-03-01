import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv
import openai
from llama_index.llms.openai import OpenAI


# Authenticate and create the Google Drive client instance
gauth = GoogleAuth()
drive = GoogleDrive(gauth)


# Load environment variables from the .env file
load_dotenv() 


# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')


# Initialize the LLM with the specified model and temperature
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")


# Import the GoogleDriveReader from llama_index to read documents from Google Drive
from llama_index.readers.google import GoogleDriveReader



# Create an instance of GoogleDriveReader
loader = GoogleDriveReader()


# Define a function to load documents from a specified Google Drive folder
def load_data(folder_id: str):
    # Use the loader to fetch documents from the given folder ID
	docs = loader.load_data(folder_id=folder_id)
	return docs




# This is the code to fetch multiple documents from the google drive by folder id.








