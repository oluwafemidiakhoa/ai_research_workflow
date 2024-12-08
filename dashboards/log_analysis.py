# dashboards/log_analysis.py

import logging
import re
from collections import Counter
import os
import schedule
import time

def setup_logger():
    """Set up the logging configuration."""
    logging.basicConfig(
        filename='logs/ai_research.log',
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def analyze_logs():
    """Analyze the log file to identify patterns and recurring issues."""
    log_file_path = 'logs/ai_research.log'
    if not os.path.exists(log_file_path):
        logging.error("Log file not found. Log analysis aborted.")
        print("Log file not found. Please ensure that the research process has been run at least once.")
        return

    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    # Define patterns to search for
    patterns = {
        "Total Errors Detected": r"Error detected",
        "Incomplete Results": r"Incomplete result",
        "Agent Errors": r"encountered an error",
        "Total Retries": r"Retrying \(\d+/\d+\)"
    }

    analysis_results = {}

    for key, pattern in patterns.items():
        matches = re.findall(pattern, ''.join(logs))
        analysis_results[key] = len(matches)

    # Additional Analysis: Errors per Agent
    agent_error_pattern = r"(\w+ AI): (Error detected|Incomplete result)"
    agent_errors = re.findall(agent_error_pattern, ''.join(logs))
    agent_error_counts = Counter([f"{agent}: {error}" for agent, error in agent_errors])
    analysis_results["Errors per Agent"] = dict(agent_error_counts)

    # Compile analysis report
    report_content = "### Log Analysis Report ###\n\n"
    report_content += f"**Total Errors Detected:** {analysis_results.get('Total Errors Detected', 0)}\n\n"
    report_content += f"**Incomplete Results:** {analysis_results.get('Incomplete Results', 0)}\n\n"
    report_content += f"**Agent Errors:** {analysis_results.get('Agent Errors', 0)}\n\n"
    report_content += f"**Total Retries:** {analysis_results.get('Total Retries', 0)}\n\n"
    
    if analysis_results.get("Errors per Agent"):
        report_content += "**Errors per Agent:**\n"
        for agent, count in analysis_results["Errors per Agent"].items():
            report_content += f"- {agent}: {count}\n"
    else:
        report_content += "**Errors per Agent:** No errors recorded.\n"

    # Save the analysis report to a text file
    report_dir = 'reports'
    os.makedirs(report_dir, exist_ok=True)  # Ensure the reports directory exists
    report_filename = os.path.join(report_dir, "log_analysis_report.txt")
    with open(report_filename, 'w') as report_file:
        report_file.write(report_content)

    print(f"Log analysis completed successfully. Report saved to {report_filename}")
    logging.info(f"Log analysis completed successfully. Report saved to {report_filename}")

def schedule_log_analysis():
    """Schedule the log analysis to run weekly on Mondays at 10 AM."""
    schedule.every().monday.at("10:00").do(analyze_logs)
    print("Log analyzer is running and scheduled to analyze logs every Monday at 10 AM.")
    logging.info("Log analyzer scheduled to run every Monday at 10 AM.")

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    setup_logger()
    schedule_log_analysis()
