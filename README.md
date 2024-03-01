## Demo Video link
https://drive.google.com/drive/folders/1hDOR39f6XbWp-Mo9KzZamUOXBBGFGpXd?usp=sharing

## Below GitHub are of my practice
https://github.com/Vi-vek9135/Project


Firstly, I thoroughly reviewed the project and understand what needs to be done and how to execute it. Afterward, I broke down the project into small tasks, which I am detailing stepwise.
Setup instructions:
1.	First clone the repo then create virtual environment in same directory.
2.	Create a conda virtual environment of python version 3.10.0
conda create -p venvIntell python==3.10.0
conda activate path/of/venvIntell

3.	Install the requirements.txt by using 
pip install -r requirements.txt

4.	Please create .env file to store openai API KEY
5.	Please change the folder_id of Automate_Data_Storage_and_Indexing.py in line no. 35 
docs = load_data(folder_id="1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL")

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

6.	Then run quickstart.py to authenticate with google drive
7.	Next run main.py
8.	Wait for some time then you are ready to chat with your own documents 
9.	Now you can ask your questions 










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
