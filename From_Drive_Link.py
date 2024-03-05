import re
import streamlit as st








# Function to parse folder ID from Google Drive link
def parse_folder_id(folder_link: str) -> str:
    match = re.search(r'/folders/([^/?]+)', folder_link)
    return match.group(1) if match else None

@st.cache_resource(experimental_allow_widgets=False)

def returnfolder_id():

    folder_link = st.text_input("Enter your Google Drive folder link:")
    if folder_link:
                folder_id = parse_folder_id(folder_link)
                if folder_id:
                    return folder_id
                


# print(returnfolder_id())