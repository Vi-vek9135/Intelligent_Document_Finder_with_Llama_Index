from llama_index.readers.microsoft_onedrive import OneDriveReader


from dotenv import load_dotenv
import os

load_dotenv() 


client_id = os.getenv('client_id')

print(client_id)

# User Authentication flow: Replace client_id with your own id
loader = OneDriveReader(client_id=f"{client_id}")



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

# Get all documents including subfolders with specified MIME types
def return_docs_from_onedrive():
    documents = loader.load_data(mime_types=mime_types)
    return documents

# print(documents)     ## This is for testing purposes only.










