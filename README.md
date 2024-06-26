
## Intelligent_Document_Finder_with_Llama_Index (File Structure)
# ├── Onedrive
# │   ├── Testing_Of_Llamahub.py    
# ├── User
# │   ├── main.py            
# │   ├── auth_bearer.py             
# │   ├── database.py            
# │   ├── models.py   
# │   ├── schemas.py
# │   └── utils.py
# │
# ├── venvIntell
# ├── Automate_Data_Storage_and_Indexing.py
# ├── client_secrets.json
# ├── credentials.json
# ├── creds.txt
# ├── From_Drive_Link.py
# ├── Frontend_Part_By_Using_Streamlit.py
# ├── main.py
# ├── quickstart.py
# ├── realtime.py
# ├── requirements.txt
# ├── To_Fetch_Multiples_documents_from_drive.py
# ├── token.json
# ├── .env
# ├── run.py
# ├── drive_testing.py


                   




## Demo Video link of Sign-Up
https://drive.google.com/file/d/1c0corTdsxXJC98o0wM8qRjK0uf_AuwYI/view?usp=sharing


## Demo Video link
https://drive.google.com/drive/folders/1hDOR39f6XbWp-Mo9KzZamUOXBBGFGpXd?usp=sharing

## Below GitHub are of my practice
https://github.com/Vi-vek9135/Project


Added Features: Login/Signup
Registration (Signup)
Click on the "Register" button in the Streamlit app.
Fill in the registration form with a unique username, email, and password.
Click the "Register" button to create a new user account.
Upon successful registration, you will be automatically logged in.

Login
Click on the "Login" button in the Streamlit app.
Enter your registered email and password.
Click the "Login" button.
Upon successful login, you will have access to the document search functionality.

User can ask any queries by entering selecting their drive (Google drive or OneDrive) 


Logout
Click on the "Logout" button to log out of your user account.
Project Integration
The FastAPI backend handles user registration, login, and logout, storing user data in a SQLite database.
Streamlit communicates with the backend using RESTful API endpoints.
OpenAI's GPT-3.5 Turbo powers the document search functionality.
User authentication is implemented using JWT (JSON Web Tokens).
The existing document search functionality remains intact, enhanced with user-specific interactions.



Firstly, I thoroughly reviewed the project and understand what needs to be done and how to execute it. Afterward, I broke down the project into small tasks, which I am detailing stepwise.
Step 1 : Setup instructions:
1.	First clone the repo then create virtual environment in same directory.
2.	Create a conda virtual environment of python version 3.10.0
conda create -p venvIntell python==3.10.0
conda activate path/of/venvIntell

3.	Install the requirements.txt by using 
pip install -r requirements.txt

4.	Please create .env file to store openai API KEY and client_id


Step 2: Fetching Documents from Google Drive and One Drive
This is for Google Drive
      1. Developed a separate file for this task.
      2. Retrieved various file types from Google Drive using the GoogleDriveReader.
      3. Authenticated with Google and saved credentials.
      •	Downloaded the `credentials.json` file following the instructions (https://developers.google.com/drive/api/v3/quickstart/python).
      •	Copied and renamed the `credentials.json` file to `client_secrets.json` for use by PyDrive.
      •	Note: Both files are essentially the same but required with different names according to the libraries used.
      4. Followed the instructions in [base.py] 
      (https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/drive/base.py) for authentication.
      Run the quickstart.py .
      After running this token.json will be created. 
      6.	Then run quickstart.py to authenticate with google drive

This is for Onedrive
      1. Create account in https://entra.microsoft.com/
      2. Then register an application with following below instructions
          User Authentication: Browser based authentication:
              You need to create a app registration in Microsoft Entra (formerly Azure Active Directory)
              For interactive authentication to work, a browser is used to authenticate, hence the registered application should have a redirect URI set to 'https://localhost' under                   mobile and native applications.
              This mode of authentication is not suitable for CI/CD or other background service scenarios where manual authentication isn't feasible.
              API Permission required for registered app:
              Microsoft Graph --> Delegated Permission -- > Files.Read.All
      3. Create separate file for loading data from onedrive

Step 3: Import the docs accordingly
Step 4: After that you have to run run.py(main file)
Step 5: Wait for some time then after login you will see two option one for onedrive and one for google drive (Select accordingly)
Step 6: tHEN you are ready to use this applicatiion
Step 7: Now you can ask your questions












Step 1: Setting Up Environment
1. Created a Conda virtual environment with Python version 3.10.0.
2. Installed the required dependencies from the `requirements.txt` file.
3. Stored the OpenAI API KEY in the `.env` file.
4. Utilized GPT-3.5 LLM for this project.

Step 2: Fetching Documents from Google Drive
1. Developed a separate file for this task.
2. Retrieved various file types from Google Drive using the GoogleDriveReader.
3. Authenticated with Google and saved credentials.
•	Downloaded the `credentials.json` file following the instructions (https://developers.google.com/drive/api/v3/quickstart/python).
•	Copied and renamed the `credentials.json` file to `client_secrets.json` for use by PyDrive.
•	Note: Both files are essentially the same but required with different names according to the libraries used.
4. Followed the instructions in [base.py] 
(https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/drive/base.py) for authentication.
Run the quickstart.py .
After running this token.json will be created. 
5. Created a function (`load_data`) to load documents by folder ID and return the documents.

Step 3: Indexing the Documents
1. Developed a separate file for this task.
2. Used the `VectorStoreIndex` to index the returned documents.
3. Returned the indexing part with the help of a function.
from To_Fetch_Multiples_documents_from_drive import load_data

Created a custom function using `@st.cache_resource(show_spinner=False)` as a decorator to cache the resource and avoid unnecessary computations during subsequent executions. The `show_spinner=False` parameter hides the spinner during caching.
import_docs_by_fetching_documents_from_drive()
A function for importing documents by fetching them from Google Drive:

•	Used `with st.spinner(text="Loading and indexing your docs – hang tight! This should take 1-2 minutes.")` to display a spinner during the loading process with a specified loading message.

Step 4: Frontend Part and Extraction of Metadata
Developed a separate file for this step. In this phase, users can ask questions about their documents, and the model will provide answers along with relevant metadata (file_name, file_type, page_number, author, etc.).

•	Provided a text input box with Streamlit to allow users to ask questions.
•	Explained on the UI what prompts to write for better answers.

Configured Streamlit page settings, including title, icon, layout, and initial sidebar state. Displayed the title for the chat application.

•	If the chat messages history is not present in the session state, initialized it with a default message.
•	Imported documents and built an index using the `import_docs_by_fetching_documents_from_drive` function.
•	If the chat engine is not present in the session state, initialized it using the Llama Index with specified chat mode and verbosity.

Prompted the user for input using Streamlit's `chat_input`.

•	Iterated through prior chat messages and displayed them.
•	If the last message is not from the assistant, generated a response using the chat engine.
•	Displayed the response and appended it to the chat messages history.
•	Displayed metadata for each source node in the response.
