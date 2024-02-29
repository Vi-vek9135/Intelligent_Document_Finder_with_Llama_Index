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