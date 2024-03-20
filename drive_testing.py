# import os
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from dotenv import load_dotenv
# import openai
# from llama_index.llms.openai import OpenAI


# # Authenticate and create the Google Drive client instance
# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)


# # Load environment variables from the .env file
# load_dotenv() 


# # Set the OpenAI API key from the environment variable
# openai.api_key = os.getenv('OPENAI_API_KEY')


# # Initialize the LLM with the specified model and temperature
# llm = OpenAI(temperature=0, model="gpt-3.5-turbo")


# # Import the GoogleDriveReader from llama_index to read documents from Google Drive
# from llama_index.readers.google import GoogleDriveReader



# # Create an instance of GoogleDriveReader
# loader = GoogleDriveReader()


# Define a function to load documents from a specified Google Drive folder
# def load_data(folder_id: str):
#     # Use the loader to fetch documents from the given folder ID
# 	docs = loader.load_data(folder_id=folder_id)
# 	return docs


# print(load_data())

# This is the code to fetch multiple documents from the google drive by folder id.




# def load_data_from_root():
#     # Use the loader to fetch documents from the root directory
#     docs = loader.load_data(folder_id='root')
#     return docs

# print(load_data_from_root())











import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv
import openai
from llama_index.llms.openai import OpenAI
from llama_index.readers.google import GoogleDriveReader

# Authenticate and create the Google Drive client instance
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the LLM with the specified model and temperature
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")

# Create an instance of GoogleDriveReader
loader = GoogleDriveReader()

# MIME types for the desired file types
mime_types = [
    "application/pdf",
    "text/plain",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/vnd.ms-powerpoint",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.ms-excel"
]

def load_data_from_root(mime_types=mime_types):
    # Use the loader to fetch documents from the root directory with specified MIME types
    docs = loader.load_data(folder_id='root', mime_types=mime_types)
    return docs

# print(load_data_from_root())








