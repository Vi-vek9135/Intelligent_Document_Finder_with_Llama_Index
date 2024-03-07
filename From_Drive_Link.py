



import re
import streamlit as st

# Function to extract the folder ID from a Google Drive link
def parse_folder_id(folder_link: str) -> str:

    # Regular expression to match the folder ID pattern within the link
    match = re.search(r'/folders/([^/?]+)', folder_link)

    # If the pattern is found, extract the folder ID from the match object
    return match.group(1) if match else None





# Function to get the folder ID from user input in Streamlit
def returnfolder_id():
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



# Below code are for testing the returnfolder_id function
# def main():
#     folder_id = returnfolder_id()
#     if folder_id:
#         st.write(f"The folder ID is: {folder_id}")

if __name__ == "__main__":
    main()
