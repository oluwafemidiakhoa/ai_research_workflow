# dashboard.py
import streamlit as st
import pandas as pd
import logging

# Configure logging to a file
logging.basicConfig(filename='ai_research.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

st.title("AI Research Workflow Dashboard")

# Function to read the log file and parse relevant information
def read_logs():
    try:
        with open('ai_research.log', 'r') as file:
            logs = file.readlines()
        return logs
    except FileNotFoundError:
        return []

logs = read_logs()

# Parse logs for agent statuses
agent_status = {}
for log in logs:
    if "is performing task" in log:
        agent = log.split(" is performing task")[0]
        agent_status[agent] = "In Progress"
    elif "Result from" in log:
        agent = log.split("Result from ")[1].split(":")[0]
        outcome = log.split(": ")[-1].strip()
        agent_status[agent] = outcome
    elif "is adjusting strategy" in log:
        agent = log.split(" is adjusting strategy")[0]
        agent_status[agent] = "Adjusting Strategy"
    elif "is generating a new hypothesis" in log:
        agent = log.split(" is generating a new hypothesis")[0]
        agent_status[agent] = "Generating Hypothesis"

# Display agent statuses
st.header("Agent Statuses")
status_df = pd.DataFrame(list(agent_status.items()), columns=["Agent", "Status"])
st.table(status_df)

# Display recent alerts
st.header("Recent Alerts")
alerts = [log for log in logs if "Alert!" in log or "WARNING" in log or "ERROR" in log]
for alert in alerts[-5:]:  # Show last 5 alerts
    st.warning(alert.strip())

# Display generated hypotheses
st.header("Generated Hypotheses")
hypotheses = [log.split("Generated Hypothesis: ")[1].strip() for log in logs if "Generated Hypothesis: " in log]
for hyp in hypotheses[-5:]:  # Show last 5 hypotheses
    st.success(hyp)
