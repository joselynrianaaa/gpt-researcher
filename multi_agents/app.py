# app.py
import streamlit as st
import os
import asyncio

# Import main functionalities from the existing multi-agent setup
from multi_agents.main import open_task  # Adjust this based on actual available functions

# Title and description for the Streamlit app
st.title("GPT Researcher Multi-Agent System")
st.write("This application allows interaction with a multi-agent system designed for research tasks.")

# Add user inputs if required
task_name = st.text_input("Enter the task name", "Example Task")
user_input = st.text_area("Input text for processing")

# Run the main task function when button is clicked
if st.button("Run Task"):
    # Call the main function from the imported script and display results
    try:
        # Ensure the environment is loaded if needed, or any async call handling
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        task_result = loop.run_until_complete(open_task(task_name, user_input))  # Pass inputs if open_task takes them
        
        # Display the results
        st.write("Task Completed!")
        st.write(task_result)  # Adjust according to what open_task returns
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Optionally display logs or other details if available
if st.checkbox("Show Logs"):
    log_path = "path_to_logs.log"  # Replace with actual log file path if it exists
    if os.path.exists(log_path):
        with open(log_path, "r") as log_file:
            logs = log_file.read()
        st.text_area("Logs", logs, height=300)
    else:
        st.write("Log file not found.")
