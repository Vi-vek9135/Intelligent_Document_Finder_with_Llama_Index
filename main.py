import subprocess

# Define the path to your Streamlit script
streamlit_script_path = 'Fronted_Part_By_Using_Streamlt.py'

# Use subprocess.Popen to execute the "streamlit run" command without blocking
process = subprocess.Popen(['streamlit', 'run', streamlit_script_path])

# ... your other code can run here while the Streamlit app is running ...

# If you need to stop the Streamlit server programmatically, you can use:
# process.terminate()

