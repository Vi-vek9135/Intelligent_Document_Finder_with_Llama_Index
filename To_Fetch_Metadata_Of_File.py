# from Fronted_Part_By_Using_Streamlt import reutrn_response
# from llama_index.llms.openai import OpenAI
# from dotenv import load_dotenv
# import openai
# import os

# load_dotenv()  # Load the .env file

# openai.api_key = os.getenv('OPENAI_API_KEY')

# llm = OpenAI(temperature=0, model="gpt-3.5-turbo")

# import streamlit as st

# response = reutrn_response()






# # Print information about source nodes
# def metadata():
#     for node in response.source_nodes:
#         st.write("-----")
#         text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
#         st.write(f"Text:\t {text_fmt} ...")
#         st.write(f"Metadata:\t {node.node.metadata}")
#         st.write(f"Score:\t {node.score:.3f}")































# from llama_index.core import (
#     SimpleDirectoryReader,
#     VectorStoreIndex,
#     download_loader,
#     RAKEKeywordTableIndex,
# )

# from llama_index.llms.openai import OpenAI

# import openai

# # import sys
# # sys.path.append("D:/Vivek_Roushan/Llama_Index/Project/To_Upload_documents_in_Drive") 

# # from Download import get_file_list


# # folder_id = '1uCxh7jmHBzU0ZUNix901qq2qkjkYHJPL'
# # file_list = get_file_list(folder_id)

# # Now you can use the file_list in the second file
# # for index, file in enumerate(file_list):
# #     print(index + 1, 'file downloaded : ', file['title'])
#     # Do whatever you want with the file_list in the second file



# # import os
# # from dotenv import load_dotenv

# # load_dotenv()  # Load the .env file

# # openai.api_key = os.getenv('OPENAI_API_KEY') 
# openai.api_key = "sk-"

# llm = OpenAI(temperature=0, model="gpt-3.5-turbo")

# reader = SimpleDirectoryReader(input_files=["data/bharat_text.pdf"])
# # reader = SimpleDirectoryReader(input_files=["file_list"])
# data = reader.load_data()

# # for file in file_list:
# #     title = file['title']
    
# #     # Get the content string without downloading the file
# #     content_string = file.GetContentString()
    
# #     # Use SimpleDirectoryReader to load data from the content string
# #     reader = SimpleDirectoryReader(data=content_string)
# #     data = reader.load_data()
    
# #     # Now you can use 'data' as needed
# #     # print(f"Data loaded from {title}")


# index = VectorStoreIndex.from_documents(data)

# query_engine = index.as_query_engine(streaming=True, similarity_top_k=3)

# response = query_engine.query(
#     "What is Section 138?"
#     " page reference after each statement."
# )

# response.print_response_stream()

# for node in response.source_nodes:
#     print("-----")
#     text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
#     print(f"Text:\t {text_fmt} ...")
#     print(f"Metadata:\t {node.node.metadata}")
#     print(f"Score:\t {node.score:.3f}")
