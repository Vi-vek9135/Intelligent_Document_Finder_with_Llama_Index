# To access text-based files (documents, code files, etc.) in your OneDrive using Python, 
# you can make use of the OneDrive API provided by Microsoft. Here's a general outline of the steps you'll need to follow:

# 1. **Register an Application**: First, you need to register an application with Microsoft Azure 
# Active Directory (Azure AD) to obtain the necessary credentials (client ID and client secret) for authentication. 
# You can do this through the Azure Portal.

# 2. **Install the Required Libraries**: You'll need to install the Microsoft Graph API client library for Python. 
# You can install it using pip:

# ```
# pip install msgraph-core
# ```

# 3. **Authenticate with OneDrive API**: Use the client ID and client secret obtained in step 1 to authenticate with the OneDrive API. 
# The authentication process involves obtaining an access token, which will be used in subsequent requests to the API.

# 4. **List Files and Folders**: Use the Microsoft Graph API to list the files and folders in your OneDrive. 
# You can filter the results to include only text-based files if needed.

# 5. **Download Files**: Once you have the list of files you want to access, you can use the API to download the file content.

# Here's some sample code to get you started:

# ```python
# from msgraph import GraphCore
# from msgraph.auth import TokenCredentialAuthProvider


# # Configure the client credentials
# client_id = 'YOUR_CLIENT_ID'
# client_secret = 'YOUR_CLIENT_SECRET'
# tenant_id = 'YOUR_TENANT_ID'

# # Authenticate with the Microsoft Graph API
# auth_provider = TokenCredentialAuthProvider(
#     client_id=client_id,
#     client_secret=client_secret,
#     tenant_id=tenant_id
# )
# graph = GraphCore(auth_provider=auth_provider)

# # List files in the root directory
# files = graph.get('/me/drive/root/children', query_params={'$select': 'name,file'})

# # Filter for text-based files
# text_files = [file for file in files if file.get('file') and not file['file']['@microsoft.graph.downloadUrl'].endswith(('.png', '.jpg', '.mp3', '.mp4'))]

# # Download a text file
# for file in text_files:
#     file_name = file['name']
#     file_content = graph.get(file['file']['@microsoft.graph.downloadUrl'])
#     with open(file_name, 'wb') as f:
#         f.write(file_content)
# # ```

# Note that this is just a basic example, and you may need to handle additional scenarios like pagination, error handling, 
# and more, depending on your specific requirements. Additionally, make sure to replace `'YOUR_CLIENT_ID'`, `'YOUR_CLIENT_SECRET'`, 
# and `'YOUR_TENANT_ID'` with your actual client ID, client secret, and tenant ID obtained from the Azure Portal.










# python -m pip install msgraph-core
# python -m pip install azure-identity

# from azure.identity import ClientSecretCredential
# from msgraph.core import GraphClient

# client_secret_credential = ClientSecretCredential(
#     tenant_id='XXX',
#     client_id='XXX',
#     client_secret='XXX')

# client = GraphClient(credential=client_secret_credential)

# result = client.get(
#     '/groups',
#     params={
#         '$select': 'displayName',
#         '$top': '10'
#     },
# )
# pprint(result.json())










# import os

# from msgraph_sdk import GraphCore
# from msgraph_sdk.auth import TokenCredentialAuthProvider

# def get_onedrive_text_files(client_id, client_secret, tenant_id):
#     """
#     Fetches text-based files from OneDrive, excluding videos, audio, and images.

#     Args:
#         client_id (str): Your Azure application client ID.
#         client_secret (str): Your Azure application client secret.
#         tenant_id (str): Your Azure Active Directory tenant ID.

#     Returns:
#         list: A list of dictionaries containing file information (name, download URL).
#     """

#     # Authenticate with Microsoft Graph API
#     auth_provider = TokenCredentialAuthProvider(
#         client_id=client_id,
#         client_secret=client_secret,
#         tenant_id=tenant_id
#     )
#     graph = GraphCore(auth_provider=auth_provider)

#     # Get all files in the root directory (adjust query_params for specific folders)
#     files = graph.get('/me/drive/root/children', query_params={'$select': 'name,file'})

#     # Filter for text-based files, excluding media extensions
#     text_files = [
#         {
#             'name': file['name'],
#             'download_url': file['file']['@microsoft.graph.downloadUrl']
#         }
#         for file in files
#         if file.get('file')
#         and not file['file']['@microsoft.graph.downloadUrl'].endswith(
#             ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg', '.mp3', '.m4a', '.wav', '.flac', '.wma', '.mp4', '.mov', '.avi', '.wmv', '.mkv', '.flv'))
#     ]

#     return text_files

# def download_text_files(text_files, download_directory):
#     """
#     Downloads text-based files from OneDrive to the specified directory.

#     Args:
#         text_files (list): A list of dictionaries containing file information.
#         download_directory (str): The path to the directory where files will be saved.
#     """

#     os.makedirs(download_directory, exist_ok=True)  # Create directory if it doesn't exist

#     for file in text_files:
#         file_name = file['name']
#         download_url = file['download_url']

#         # Download the file using requests or another preferred library
#         # (replace with your preferred download method)
#         response = requests.get(download_url)

#         if response.status_code == 200:
#             with open(os.path.join(download_directory, file_name), 'wb') as f:
#                 f.write(response.content)
#             print(f"Downloaded: {file_name}")
#         else:
#             print(f"Error downloading {file_name}: {response.status_code}")

# if __name__ == '__main__':
#     # Replace with your Azure application credentials
#     client_id = '3a6f7573-fb1f-4856-84ed-cd30273b4a6f'
#     client_secret = 'f9e1b16c-d1c5-4b95-9c53-3d69fbb40009'
#     tenant_id = '6f0e257a-ff8e-428f-9b09-54c1c3a7950c'

#     # Specify the download directory
#     download_directory = 'your_download_directory'  # Replace with your desired path

#     text_files = get_onedrive_text_files(client_id, client_secret, tenant_id)
#     download_text_files(text_files, download_directory)











# import os
# from requests_oauthlib import OAuth2Session

# # Define your Microsoft application's credentials
# client_id = '3a6f7573-fb1f-4856-84ed-cd30273b4a6f'
# client_secret = 'f9e1b16c-d1c5-4b95-9c53-3d69fbb40009'
# redirect_uri = 'http://localhost:8080'  # This needs to be added in your Azure app registration

# # Define required Microsoft Graph endpoints
# authorize_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
# token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
# graph_api_endpoint = 'https://graph.microsoft.com/v1.0/'

# # Define the scopes required for OneDrive access
# scopes = ['files.read.all']

# # Initialize OAuth2 session
# oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)

# # Get the authorization URL
# authorization_url, state = oauth.authorization_url(authorize_url)

# # Direct the user to the authorization URL for Microsoft login
# print("Please go to this URL and authorize access:", authorization_url)
# authorization_response = input("Paste the full redirect URL here: ")

# # Fetch the access token
# token = oauth.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret)

# # Fetch the list of files from OneDrive
# response = oauth.get(graph_api_endpoint + 'me/drive/root/children')
# data = response.json()

# # Process the files
# for file_data in data['value']:
#     file_name = file_data['name']
#     file_type = file_data['file']['mimeType']

#     # Check if it's a text-based file
#     if 'text' in file_type:
#         file_id = file_data['id']
#         download_url = graph_api_endpoint + f'me/drive/items/{file_id}/content'
        
#         # Download the text-based file
#         file_content = oauth.get(download_url).text
        
#         # Do something with the file content, for example, print it
#         print(f"File Name: {file_name}")
#         print("Content:")
#         print(file_content)
#         print("\n")

# # Note: You may need to handle pagination if you have a large number of files.








# from msgraph_sdk import GraphCore
# from msgraph_sdk.auth import TokenCredentialAuthProvider

# # Configure the client credentials (replace with your own)
# client_id = '3a6f7573-fb1f-4856-84ed-cd30273b4a6f'
# client_secret = 'f9e1b16c-d1c5-4b95-9c53-3d69fbb40009'
# tenant_id = '6f0e257a-ff8e-428f-9b09-54c1c3a7950c'

# # Authenticate with the Microsoft Graph API
# auth_provider = TokenCredentialAuthProvider(
#     client_id=client_id,
#     client_secret=client_secret,
#     tenant_id=tenant_id
# )
# graph = GraphCore(auth_provider=auth_provider)

# # List files in the root directory (or specific folder path)
# files = graph.get('/me/drive/root/children', query_params={'$select': 'name,file'})  # Adjust path if needed

# # Filter for text-based files
# text_file_extensions = ('.txt', '.docx', '.pdf', '.rtf', '.odt', '.csv')  # Add more as needed
# text_files = [
#     file for file in files
#     if file.get('file')
#     and not file['file']['@microsoft.graph.downloadUrl'].endswith(text_file_extensions)
#     and not file['file']['@microsoft.graph.downloadUrl'].endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.mp3', '.mp4', '.wav', '.flac'))
# ]

# # Download the text files
# for file in text_files:
#     file_name = file['name']
#     file_content = graph.get(file['file']['@microsoft.graph.downloadUrl'])

#     with open(file_name, 'wb') as f:
#         f.write(file_content)

# print(f"Downloaded {len(text_files)} text files.")











import requests
from requests_oauthlib import OAuth2Session

# Replace these with your app's client ID, client secret, and redirect URI
client_id = '3a6f7573-fb1f-4856-84ed-cd30273b4a6f'
client_secret = 'f9e1b16c-d1c5-4b95-9c53-3d69fbb40009'
redirect_uri = 'http://localhost:8080'

# Construct the authentication URL and obtain the authorization code
auth_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
auth_data = {
    'response_type': 'code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'scope': 'https://graph.microsoft.com/Files.Read.All offline_access'
}

# Redirect the user to the authentication URL
print(f'Please visit this URL to authenticate:\n{auth_url}?{requests.PreparedRequest().prepare_url(auth_data, {})}')
auth_code = input('Enter the authorization code: ')

# Exchange the authorization code for an access token
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
token_data = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'scope': 'https://graph.microsoft.com/Files.Read.All offline_access'
}

token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()['access_token']

# Create an OAuth2Session and use it to send requests to the Graph API
session = OAuth2Session(client_id, token=access_token)

# Read files from OneDrive
files_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
files_response = session.get(files_url)
files_data = files_response.json()['value']

# Print the names of the files
for file in files_data:
    print(file['name'])