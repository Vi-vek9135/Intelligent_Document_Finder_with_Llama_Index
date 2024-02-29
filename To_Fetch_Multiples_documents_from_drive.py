# import os
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from dotenv import load_dotenv
# import openai
# from llama_index.llms.openai import OpenAI

# llm = OpenAI(temperature=0, model="gpt-3.5-turbo")

# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)


# load_dotenv()  # Load the .env file

# openai.api_key = os.getenv('OPENAI_API_KEY')

# from llama_index.readers.google import GoogleDriveReader


# loader = GoogleDriveReader()

# def load_data(folder_id: str):
# 	docs = loader.load_data(folder_id=folder_id)
# 	# for doc in docs:
# 	# 	doc.id_ = doc.metadata["file_name"]
# 		# doc.id_ = doc.metadata["bharat_text"]
# 	return docs




# This is the code to fetch multiple documents from the google drive by folder id.









# #This is for download files from google drive in local directory

# import os
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)

# folder = '1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL'


# # Download files
# file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
# for index, file in enumerate(file_list):
# 	print(index+1, 'file downloaded : ', file['title'])
# 	file.GetContentFile(file['title'])








# This is for uploading the files to the google drive by folder id.

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL'

# file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello2.txt'})
# file1.SetContentString('Hello world!, this is my second file')
# file1.Upload()





# Upload files
directory = "D:/Vivek_Roushan/docs"

for f in os.listdir(directory):
	filename = os.path.join(directory, f)
	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
	gfile.SetContentFile(filename)
	gfile.Upload()
