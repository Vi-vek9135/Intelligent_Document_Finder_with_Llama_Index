# from llama_index.readers.microsoft_onedrive import OneDriveReader

# # User Authentication flow: Replace client id with your own id
# loader = OneDriveReader(client_id="acdc67b7-9781-4e11-afb9-0c8f4180de9b")

# # APP Authentication flow: NOT SUPPORTED By Microsoft

# #### Get all documents including subfolders.
# documents = loader.load_data()

# print(documents)




# from llama_index.readers.microsoft_onedrive import OneDriveReader

# # User Authentication flow: Replace client id with your own id
# loader = OneDriveReader(client_id="acdc67b7-9781-4e11-afb9-0c8f4180de9b")

# # Get all documents including subfolders
# all_documents = loader.load_data()

# # Define the allowed file extensions
# allowed_extensions = ['.pdf', '.pptx', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.html', '.csv', '.xml']

# # Filter the documents based on file extension
# # filtered_documents = [doc for doc in all_documents if any(doc.source_path.endswith(ext) for ext in allowed_extensions)]
# filtered_documents = [doc for doc in all_documents if any(doc.source_node.endswith(ext) for ext in allowed_extensions)]

# print(filtered_documents)






from llama_index.readers.microsoft_onedrive import OneDriveReader

# User Authentication flow: Replace client id with your own id
loader = OneDriveReader(client_id="acdc67b7-9781-4e11-afb9-0c8f4180de9b")

# Define the allowed file extensions
allowed_extensions = ['.pdf', '.pptx', '.docx', '.txt', '.xlsx', '.xls', '.html', '.csv', '.xml']

# Load data from OneDrive
documents = loader.load_data()

# Filter documents based on allowed extensions
filtered_documents = []

for doc in documents:
    if hasattr(doc, 'name') and any(doc.name.lower().endswith(ext) for ext in allowed_extensions):
        filtered_documents.append(doc)

print(filtered_documents)

