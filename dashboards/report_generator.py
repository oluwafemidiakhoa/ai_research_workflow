# dashboards/report_generator.py

import logging
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import re
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

def generate_report():
    """Generate a PDF report summarizing the AI research workflow."""
    # Read the log file
    log_file_path = 'logs/ai_research.log'
    if not os.path.exists(log_file_path):
        logging.error("Log file not found. Report generation aborted.")
        print("Log file not found. Please ensure that the research process has been run at least once.")
        return

    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    # Initialize report content
    report_content = "AI Research Workflow Report\n\n"

    # Extract task outcomes
    valid_results = []
    error_results = []
    hypotheses = []

    for log in logs:
        if "Result from" in log:
            # Example log entry: "2024-04-27 10:00:00:INFO:Result from Bioinformatics AI: Valid result"
            match = re.match(r".*Result from (\w+ AI): (\w[\w\s]*)", log)
            if match:
                agent = match.group(1)
                outcome = match.group(2)
                if outcome in ["Valid result", "New hypothesis formed"]:
                    valid_results.append(f"{agent}: {outcome}")
                elif outcome in ["Error detected", "Incomplete result"]:
                    error_results.append(f"{agent}: {outcome}")
        if "Generated Hypothesis: " in log:
            # Example log entry: "2024-04-27 10:05:00:INFO:Generated Hypothesis: The recent advancements..."
            match = re.match(r".*Generated Hypothesis: (.*)", log)
            if match:
                hypothesis = match.group(1)
                hypotheses.append(hypothesis)

    # Compile report sections
    report_content += "### Task Outcomes:\n"
    if valid_results:
        for result in valid_results:
            report_content += f"- {result}\n"
    else:
        report_content += "- No valid results recorded.\n"

    if error_results:
        report_content += "\n### Errors Encountered:\n"
        for error in error_results:
            report_content += f"- {error}\n"
    else:
        report_content += "\n### Errors Encountered:\n- No errors encountered.\n"

    if hypotheses:
        report_content += "\n### Generated Hypotheses:\n"
        for hyp in hypotheses:
            report_content += f"- {hyp}\n"
    else:
        report_content += "\n### Generated Hypotheses:\n- No hypotheses generated.\n"

    # Create a PDF report
    report_dir = 'reports'
    os.makedirs(report_dir, exist_ok=True)  # Ensure the reports directory exists
    report_filename = os.path.join(report_dir, "AI_Research_Report.pdf")
    c = canvas.Canvas(report_filename, pagesize=letter)
    width, height = letter

    # Add report title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "AI Research Workflow Report")

    # Add report content
    c.setFont("Helvetica", 12)
    textobject = c.beginText(50, height - 80)
    for line in report_content.split('\n'):
        textobject.textLine(line)
    c.drawText(textobject)
    c.save()

    print(f"Report generated successfully: {report_filename}")
    logging.info(f"Report generated successfully: {report_filename}")

def schedule_reports():
    """Schedule the report generation to run weekly on Mondays at 9 AM."""
    schedule.every().monday.at("09:00").do(generate_report)
    print("Report generator is running and scheduled to generate reports every Monday at 9 AM.")
    logging.info("Report generator scheduled to run every Monday at 9 AM.")

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    setup_logger()
    schedule_reports()
