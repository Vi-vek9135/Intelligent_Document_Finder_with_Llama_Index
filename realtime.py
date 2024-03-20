from io import BytesIO
import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and automatically handles authentication.
drive = GoogleDrive(gauth)

# Authenticate with Google Drive
# def authenticate_drive():
#     gauth = GoogleAuth()
#     gauth.LocalWebserverAuth()  # Creates local webserver and automatically handles authentication.
#     drive = GoogleDrive(gauth)
#     return drive


# drive = authenticate_drive()  
# Fetch files from a specific folder in Google Drive
def fetch_files_from_drive(folder_id):
    # drive = authenticate_drive()
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    return file_list

# Streamlit app
def main():
    st.title("Google Drive File Fetcher")

    # Google Drive folder ID (replace with your folder ID)
    folder_id = st.text_input("Enter Google Drive Folder ID:")

    if folder_id:
        try:
            # drive = authenticate_drive()  # Define the drive variable here
            file_list = fetch_files_from_drive(folder_id)

            st.subheader("Files in the Folder:")
            for file in file_list:
                st.write(f"{file['title']} - {file['id']}")

            # Display file upload widget
            uploaded_file = st.file_uploader("Upload a new file to the folder:", type=['txt', 'pdf', 'docx'])

            if uploaded_file is not None:

                # Read the file content into a BytesIO object
                file_content = BytesIO(uploaded_file.read())

                # Upload the new file to the Google Drive folder
                gdrive_file = drive.CreateFile({'title': uploaded_file.name, 'parents': [{'id': folder_id}]})
                gdrive_file.content = file_content  # Set the content of the file
                gdrive_file.Upload()

                st.success(f"File '{uploaded_file.name}' uploaded successfully!")

                # Update the file list
                file_list = fetch_files_from_drive(folder_id)

                st.subheader("Updated Files in the Folder:")
                for file in file_list:
                    st.write(f"{file['title']} - {file['id']}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()









