# gui.py
import streamlit as st
import subprocess
import threading
import time
import os

st.title("AI Research Workflow Manager")

# Function to start the research process
def start_research():
    subprocess.Popen(["python", "main.py"])  # Assuming your main workflow script is main.py
    st.success("Research process started.")

# Function to display logs
def display_logs():
    try:
        with open('ai_research.log', 'r') as file:
            logs = file.read()
        st.text_area("Logs", logs, height=300)
    except FileNotFoundError:
        st.error("Log file not found.")

# Function to configure agent settings
def configure_agents():
    st.header("Configure Agents")
    agents = ["Immunology AI", "Bioinformatics AI", "ML AI", "Hypothesis Generator"]
    for agent in agents:
        st.subheader(agent)
        max_retries = st.number_input(f"Max Retries for {agent}", min_value=0, max_value=5, value=2, key=f"{agent}_retries")
        retry_interval = st.number_input(f"Retry Interval (seconds) for {agent}", min_value=0, max_value=10, value=1, key=f"{agent}_interval")
        # Save configurations to a file or a config object
        # For simplicity, we're not implementing saving in this snippet

# Function to generate hypothesis on-demand
def generate_hypothesis():
    if st.button("Generate Hypothesis"):
        subprocess.Popen(["python", "hypothesis_generator.py"])  # Assuming separate script
        st.success("Hypothesis generation initiated.")

# Layout
if st.button("Start Research Process"):
    start_research()

st.button("Generate Hypothesis", on_click=generate_hypothesis)

st.header("Agent Configurations")
configure_agents()

st.header("Logs")
display_logs()
