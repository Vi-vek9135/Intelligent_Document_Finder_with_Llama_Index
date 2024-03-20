import os.path
import re
import streamlit as st
from io import BytesIO
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
# https://www.googleapis.com/auth/drive
SCOPES = ["https://www.googleapis.com/auth/drive"]

# Function to extract the folder ID from a Google Drive link
def parse_folder_id(folder_link: str) -> str:
    match = re.search(r'/folders/([^/?]+)', folder_link)
    return match.group(1) if match else None

# Function to get the folder ID from user input in Streamlit
def get_folder_id():
    folder_link = st.text_input("Enter your Google Drive folder link:")

    # Check if the user entered a link
    if folder_link:
        folder_id = parse_folder_id(folder_link)

        # Handle invalid link case
        if folder_id:
            return folder_id
        else:
            st.error("Invalid Google Drive folder link.")
            return None
    else:
        # If no link is provided, ask for the folder ID directly
        folder_id = st.text_input("Enter your Google Drive folder ID:")
        if folder_id:
            return folder_id
        else:
            st.error("Please enter a valid Google Drive folder link or ID.")
            return None

# Authenticate with Google Drive using the API client library
def authenticate_drive_api():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)
        return service
    except HttpError as error:
        st.error(f"An error occurred: {error}")
        return None

# Authenticate with Google Drive using the PyDrive library
def authenticate_drive_pydrive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Creates local webserver and automatically handles authentication.
    drive = GoogleDrive(gauth)
    return drive

# Fetch files from a specific folder in Google Drive using the API client library
def fetch_files_from_drive_api(service, folder_id):
    try:
        results = (
            service.files()
            .list(
                pageSize=10,
                fields="nextPageToken, files(id, name)",
                q=f"'{folder_id}' in parents and trashed=false",
            )
            .execute()
        )
        items = results.get("files", [])
        return items
    except HttpError as error:
        st.error(f"An error occurred: {error}")
        return []

# Fetch files from a specific folder in Google Drive using the PyDrive library
def fetch_files_from_drive_pydrive(drive, folder_id):
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    return file_list

# Streamlit app
def main():
    st.title("Google Drive File Fetcher")

    # Get the folder ID from the user
    folder_id = get_folder_id()

    if folder_id:
        try:
            # Authenticate with Google Drive using both libraries
            service = authenticate_drive_api()
            drive = authenticate_drive_pydrive()

            if service and drive:
                # Fetch files from the folder using both libraries
                file_list_api = fetch_files_from_drive_api(service, folder_id)
                file_list_pydrive = fetch_files_from_drive_pydrive(drive, folder_id)

                st.subheader("Files in the Folder (API Client Library):")
                for file in file_list_api:
                    st.write(f"{file['name']} ({file['id']})")

                st.subheader("Files in the Folder (PyDrive Library):")
                for file in file_list_pydrive:
                    st.write(f"{file['title']} - {file['id']}")

                # Display file upload widget
                uploaded_file = st.file_uploader("Upload a new file to the folder:", type=['txt', 'pdf', 'docx'])

                if uploaded_file is not None:
                    # Read the file content into a BytesIO object
                    file_content = BytesIO(uploaded_file.read())

                    # Upload the new file to the Google Drive folder using PyDrive
                    gdrive_file = drive.CreateFile({'title': uploaded_file.name, 'parents': [{'id': folder_id}]})
                    gdrive_file.content = file_content  # Set the content of the file
                    gdrive_file.Upload()

                    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

                    # Update the file list using both libraries
                    file_list_api = fetch_files_from_drive_api(service, folder_id)
                    file_list_pydrive = fetch_files_from_drive_pydrive(drive, folder_id)

                    st.subheader("Updated Files in the Folder (API Client Library):")
                    for file in file_list_api:
                        st.write(f"{file['name']} ({file['id']})")

                    st.subheader("Updated Files in the Folder (PyDrive Library):")
                    for file in file_list_pydrive:
                        st.write(f"{file['title']} - {file['id']}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()