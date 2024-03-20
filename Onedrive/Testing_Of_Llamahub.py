# from llama_index.readers.microsoft_onedrive import OneDriveReader

# # User Authentication flow: Replace client id with your own id
# loader = OneDriveReader(client_id="acdc67b7-9781-4e11-afb9-0c8f4180de9b")

# # APP Authentication flow: NOT SUPPORTED By Microsoft

# #### Get all documents including subfolders.
# documents = loader.load_data()

# print(documents)





from llama_index.readers.microsoft_onedrive import OneDriveReader

# User Authentication flow: Replace client_id with your own id
loader = OneDriveReader(client_id="acdc67b7-9781-4e11-afb9-0c8f4180de9b")

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

# print(documents)











