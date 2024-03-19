# from llama_index.readers.microsoft_onedrive import OneDriveReader

# # User Authentication flow: Replace client id with your own id
# loader = OneDriveReader(client_id='3a6f7573-fb1f-4856-84ed-cd30273b4a6f', 
#                         client_secret = 'f9e1b16c-d1c5-4b95-9c53-3d69fbb40009' ,
#                         tenant_id = '6f0e257a-ff8e-428f-9b09-54c1c3a7950c'
#                         )

# # APP Authentication flow: NOT SUPPORTED By Microsoft

# #### Get all documents including subfolders.
# documents = loader.load_data()

# #### Get documents using folder_id , to exclude traversing subfolders explicitly set the recursive flag to False, default is True
# documents = loader.load_data(folder_id="6C4980918727668B%212002", recursive=False)

# #### Using file ids
# # documents = loader.load_data(file_ids=["fileid1", "fileid2"])





# import msal

# def acquire_token_func():
#     """
#     Acquire token via MSAL
#     """
#     authority_url = 'https://login.microsoftonline.com/{tenant_id_or_name}'
#     #authority_url =  'https://login.microsoftonline.com/'
#     app = msal.ConfidentialClientApplication(
        
#         #authority='https://login.microsoftonline.com/',
#         authority=authority_url,
#         client_id='3a6f7573-fb1f-4856-84ed-cd30273b4a6f',
#         client_credential='A_C8Q~ssjXEfak2gj-VzaSgsyIshs_T4xWngecM~',
#         #client_secret='A_C8Q~ssjXEfak2gj-VzaSgsyIshs_T4xWngecM~',

#         #tenant_id='6f0e257a-ff8e-428f-9b09-54c1c3a7950c',

#     )
#     token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
#     return token





# from office365.graph_client import GraphClient

# tenant_name = "contoso.onmicrosoft.com"
# client = GraphClient(acquire_token_func)
# drives = client.drives.get().execute_query()
# for drive in drives:
#     print("Drive url: {0}".format(drive.web_url))





# Define imports
import msal


# import requests

# Enter the details of your AAD app registration
client_id = '3a6f7573-fb1f-4856-84ed-cd30273b4a6f'
client_secret = 'A_C8Q~ssjXEfak2gj-VzaSgsyIshs_T4xWngecM~'
authority = 'https://login.microsoftonline.com/6f0e257a-ff8e-428f-9b09-54c1c3a7950c'
scope = ['https://graph.microsoft.com/.default']

# Create an MSAL instance providing the client_id, authority and client_credential parameters
client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

# First, try to lookup an access token in cache
token_result = client.acquire_token_silent(scope, account=None)

# If the token is available in cache, save it to a variable
if token_result:
  access_token = 'Bearer ' + token_result['access_token']
  print('Access token was loaded from cache')

# If the token is not available in cache, acquire a new one from Azure AD and save it to a variable
if not token_result:
  token_result = client.acquire_token_for_client(scopes=scope)
  access_token = 'Bearer ' + token_result['access_token']
  print('New access token was acquired from Azure AD')


# # Define Microsoft Graph API endpoint for OneDrive files
# graph_endpoint = 'https://graph.microsoft.com/v1.0/me/drive/root/children'

# # Make a request to retrieve the list of files from OneDrive
# response = requests.get(graph_endpoint, headers={'Authorization': access_token})

# # Check if the request was successful
# if response.status_code == 200:
#     files = response.json()['value']
#     for file in files:
#         print(file['name'])  # Print the name of each file
# else:
#     print('Error occurred while retrieving files:', response.text)






print(access_token)











# # Define imports
# import msal
# import requests

# # Enter the details of your AAD app registration
# client_id = '3a6f7573-fb1f-4856-84ed-cd30273b4a6f'
# authority = 'https://login.microsoftonline.com/6f0e257a-ff8e-428f-9b09-54c1c3a7950c'
# scope = ['https://graph.microsoft.com/.default']

# # Create an MSAL instance providing the client_id and authority parameters
# client = msal.PublicClientApplication(client_id, authority=authority)

# # Acquire a token for a user
# result = client.acquire_token_by_username_password(username="vivekroushan32@gmail.com", password="Vivek@85050", scopes=scope)

# # Extract the access token from the result
# if "access_token" in result:
#     access_token = result["access_token"]
#     print('Access token acquired successfully')

#     # Define Microsoft Graph API endpoint for OneDrive files
#     graph_endpoint = 'https://graph.microsoft.com/v1.0/me/drive/root/children'

#     # Make a request to retrieve the list of files from OneDrive
#     response = requests.get(graph_endpoint, headers={'Authorization': 'Bearer ' + access_token})

#     # Check if the request was successful
#     if response.status_code == 200:
#         files = response.json()['value']
#         for file in files:
#             print(file['name'])  # Print the name of each file
#     else:
#         print('Error occurred while retrieving files:', response.text)
# else:
#     print('Failed to acquire access token:', result.get("error_description"))



