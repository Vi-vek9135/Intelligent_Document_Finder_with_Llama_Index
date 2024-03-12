import subprocess
import os

def run_backend():
    os.chdir("E:/C/Promact/Project/Intelligent_Document_Finder_with_Llama_Index/User")  # Replace with the actual path to your backend folder
    subprocess.run(["uvicorn", "main:app", "--reload"])

def run_frontend():
    os.chdir("E:/C/Promact/Project/Intelligent_Document_Finder_with_Llama_Index")  # Replace with the actual path to your frontend folder
    subprocess.run(["streamlit", "run", "Fronted_Part_By_Using_Streamlt.py"])

if __name__ == "__main__":
    backend_process = subprocess.Popen(run_backend())
    frontend_process = subprocess.Popen(run_frontend())

    # try:
    #     backend_process.wait()
    # except KeyboardInterrupt:
    #     backend_process.terminate()
    #     frontend_process.terminate()
