import subprocess
import os

def run_backend():
    os.chdir("E:/C/Promact/Project/Intelligent_Document_Finder_with_Llama_Index/User")
    backend_cmd = ["uvicorn", "main:app", "--reload"]
    subprocess.run(backend_cmd)

def run_frontend():
    os.chdir("E:/C/Promact/Project/Intelligent_Document_Finder_with_Llama_Index")
    frontend_cmd = ["streamlit", "run", "Fronted_Part_By_Using_Streamlt.py"]
    subprocess.run(frontend_cmd)

if __name__ == "__main__":
    backend_process = subprocess.Popen(["uvicorn", "main:app", "--reload"], cwd="E:/C/Promact/Project/Intelligent_Document_Finder_with_Llama_Index/User")
    frontend_process = subprocess.Popen(["streamlit", "run", "Fronted_Part_By_Using_Streamlt.py"], cwd="E:/C/Promact/Project/Intelligent_Document_Finder_with_Llama_Index")

    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        backend_process.terminate()
        frontend_process.terminate()
