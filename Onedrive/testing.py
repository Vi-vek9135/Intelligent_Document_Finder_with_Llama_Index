from llama_index.readers.microsoft_onedrive import OneDriveReader

# User Authentication flow: Replace client id with your own id
loader = OneDriveReader(client_id="3a6f7573-fb1f-4856-84ed-cd30273b4a6f")

# APP Authentication flow: NOT SUPPORTED By Microsoft

#### Get all documents including subfolders.
documents = loader.load_data()

#### Get documents using folder_id , to exclude traversing subfolders explicitly set the recursive flag to False, default is True
documents = loader.load_data(folder_id="6C4980918727668B%212002", recursive=False)

#### Using file ids
# documents = loader.load_data(file_ids=["fileid1", "fileid2"])
print(documents)