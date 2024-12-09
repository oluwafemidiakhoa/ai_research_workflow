AI Research Workflow
Overview
AI Research Workflow is a Python-based application designed to orchestrate an AI-driven research process. It leverages multiple AI agents to perform specialized tasks, generate hypotheses, and manage the research workflow with both automated and human oversight. This modular and scalable system ensures efficient research execution, error handling, and continuous improvement through feedback mechanisms.

Table of Contents
Overview
Features
Directory Structure
Prerequisites
Setup Instructions
1. Clone the Repository
2. Create and Activate a Virtual Environment
3. Install Dependencies
4. Set the OpenAI API Key
Usage
Running the Research Workflow
Viewing Logs
Understanding the Outputs
Troubleshooting
Common Issues
API Key Errors
Contributing
License
Acknowledgements
Features
Modular Design: Organized into agents, managers, and utilities for maintainability and scalability.
AI Agents: Specialized agents (Immunology AI, Bioinformatics AI, ML AI, Hypothesis Generator) perform distinct research tasks.
Human Oversight: HumanResearcher class ensures critical issues are addressed promptly.
Logging Mechanism: Comprehensive logging captures all events, errors, and actions.
Feedback Loop: Continuous improvement through feedback provided by the PrincipalInvestigator.
Error Handling: Robust mechanisms to handle and log errors, with retry strategies for recoverable issues.
Directory Structure
markdown
Copy code
ai_research_workflow/
│
├── agents/
│   ├── __init__.py
│   ├── ai_agent.py
│   └── hypothesis_agent.py
│
├── managers/
│   ├── __init__.py
│   ├── principal_investigator.py
│   └── human_researcher.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
├── logs/
│   └── ai_research.log
│
├── reports/
│   └── AI_Research_Report.pdf
│
├── main.py
├── requirements.txt
└── README.md
Description of Key Components
agents/

ai_agent.py: Defines the AIAgent base class responsible for performing tasks, handling retries, and adjusting strategies based on feedback.
hypothesis_agent.py: Inherits from AIAgent and specializes in generating hypotheses using the OpenAI API.
managers/

principal_investigator.py: Manages the team of AI agents, assigns tasks, reviews results, and provides feedback.
human_researcher.py: Oversees the research process, handling human intervention when critical issues arise.
utils/

logger.py: Centralizes the logging configuration to ensure consistent and detailed logging across all modules.
logs/

ai_research.log: Stores all log entries capturing events, errors, task outcomes, and other significant actions.
reports/

AI_Research_Report.pdf: Example of a generated research report summarizing task outcomes, errors, and hypotheses.
main.py: The entry point of the application that orchestrates the entire research workflow.

requirements.txt: Lists all Python dependencies required for the application.

README.md: Provides an overview of the application, setup instructions, and usage guidelines.

Prerequisites
Before setting up the AI Research Workflow, ensure you have the following installed on your system:

Python 3.6 or higher: Download Python
Git: Download Git
OpenAI API Key: Sign up and obtain an API key from OpenAI
Setup Instructions
Follow the steps below to set up and run the AI Research Workflow on your local machine.

1. Clone the Repository
First, clone the repository to your local machine using Git.

bash
Copy code
git clone https://github.com/yourusername/ai_research_workflow.git
cd ai_research_workflow
Replace https://github.com/yourusername/ai_research_workflow.git with the actual repository URL if different.

2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

On Windows:

cmd
Copy code
python -m venv venv
venv\Scripts\activate
On Unix or MacOS:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required Python packages using pip.

bash
Copy code
pip install -r requirements.txt
requirements.txt should contain the following:

txt
Copy code
openai
Add other dependencies as needed, such as streamlit for dashboards or reportlab for report generation.

4. Set the OpenAI API Key
The application requires access to the OpenAI API. Set your API key as an environment variable to keep it secure.

On Windows (Command Prompt):

cmd
Copy code
set OPENAI_API_KEY=<your-api-key>
On Windows (PowerShell):

powershell
Copy code
$env:OPENAI_API_KEY="<your-api-key>"
On Unix or MacOS:

bash
Copy code
export OPENAI_API_KEY=<your-api-key>
Important:

Replace sk-your-api-key with your actual OpenAI API key.
Do not include quotes around the API key in Command Prompt. PowerShell allows quotes.
Ensure that you set the environment variable in the same terminal session where you will run the application.
Verify the API Key:

To confirm that the API key is set correctly, you can echo the environment variable.

On Windows (Command Prompt):

cmd
Copy code
echo %OPENAI_API_KEY%
On Windows (PowerShell):

powershell
Copy code
echo $env:OPENAI_API_KEY
On Unix or MacOS:

bash
Copy code
echo $OPENAI_API_KEY
The output should display your API key without quotes (except in PowerShell).

Usage
Once the setup is complete, you can run the AI Research Workflow.

Running the Research Workflow
Execute the main.py script to start the research process.

bash
Copy code
python main.py
What Happens:

Initialization:

Sets up logging.
Initializes AI agents with their respective tasks and configurations.
Adds agents to the team managed by the PrincipalInvestigator.
Task Execution:

Each agent performs its assigned task.
Handles retries and logs outcomes.
Result Review:

The PrincipalInvestigator reviews the results from all agents.
Provides feedback based on task outcomes.
Strategy Adjustment:

Agents adjust their strategies based on feedback.
Hypothesis Generation:

The HypothesisGenerator generates a new hypothesis using the OpenAI API.
Logs and prints the generated hypothesis.
Human Oversight:

The HumanResearcher oversees the process.
Alerts are raised for any critical issues requiring human intervention.
Final Summary:

Provides a summary of the research process and outcomes.
Sample Output:

vbnet
Copy code
Dr. James Zou is assigning tasks to AI agents...

Immunology AI (Immunology) is performing its task: Designing nanobodies for SARS-CoV-2...
Result from Immunology AI: Incomplete result
Immunology AI encountered an incomplete result. Retrying (1/1)...
Result from Immunology AI: Incomplete result
Immunology AI failed after 1 retries.
Bioinformatics AI (Computational Biology) is performing its task: Analyzing gene sequences for antiviral response...
Result from Bioinformatics AI: Error detected
Bioinformatics AI encountered a critical error.
ML AI (Machine Learning) is performing its task: Building predictive models for drug efficacy...
Result from ML AI: Incomplete result
ML AI encountered an incomplete result. Retrying (1/1)...
Result from ML AI: Incomplete result
ML AI failed after 1 retries.
Hypothesis Generator (Hypothesis Generation) is performing its task: Generating new hypotheses based on scientific data...
Result from Hypothesis Generator: Valid result

Reviewing results...

Reviewing: Incomplete result
Reviewing: Error detected
Reviewing: Incomplete result
Reviewing: Valid result

AI Research Completed: All results reviewed.

Dr. James Zou is providing feedback to Immunology AI: Ensure completeness and accuracy in your data analysis.
Immunology AI is adjusting its strategy based on feedback: Ensure completeness and accuracy in your data analysis. Specific issue: Incomplete result....

Dr. James Zou is providing feedback to Bioinformatics AI: Address the critical error encountered in data processing.
Bioinformatics AI is adjusting its strategy based on feedback: Address the critical error encountered in data processing. Specific issue: Error detected....

Dr. James Zou is providing feedback to ML AI: Ensure completeness and accuracy in your data analysis.
ML AI is adjusting its strategy based on feedback: Ensure completeness and accuracy in your data analysis. Specific issue: Incomplete result....

Dr. James Zou is providing feedback to Hypothesis Generator: Good job! Continue with the current strategy.
Hypothesis Generator is adjusting its strategy based on feedback: Good job! Continue with the current strategy....

Hypothesis Generator is generating a new hypothesis based on data from literature...
Error detected during hypothesis generation: Error code: 401 - {'error': {'message': "Incorrect API key provided: 'sk-proj...JYA'. You can find your API key at https://platform.openai.com/account/api-keys.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}}

Nyah Aduke is overseeing the research process...
Alert! The following results require human intervention:
Immunology AI: Incomplete result
Bioinformatics AI: Error detected
ML AI: Incomplete result

Human review complete. Proceeding to final conclusions.

--- Final Overview ---
AI agents have refined their strategies, and the hypothesis has been adjusted.
Generated Hypothesis: Error detected
The human researcher has ensured the research is on track.
Viewing Logs
All events, errors, and actions are logged in the logs/ai_research.log file. You can view the logs using any text editor or command-line tools.

Using Command Prompt:

cmd
Copy code
type logs\ai_research.log
Using PowerShell:

powershell
Copy code
Get-Content logs\ai_research.log
Using Notepad:

Navigate to the logs/ directory and open ai_research.log with Notepad or any preferred text editor.

Understanding the Outputs
Log File (ai_research.log): Contains detailed logs of the entire research process, including task assignments, results, retries, errors, and strategy adjustments.

Reports (reports/ directory): Although not yet implemented in the provided structure, you can extend the application to generate PDF or text reports summarizing the research progress and outcomes.

Troubleshooting
Encountering issues is a common part of development. Below are some common problems and their solutions to help you resolve them effectively.

Common Issues
'OPENAI_API_KEY' is not recognized as an internal or external command

Cause: Attempting to set environment variables using Unix-like syntax (export) on Windows Command Prompt, which does not support it.

Solution:

On Windows Command Prompt:

cmd
Copy code
set OPENAI_API_KEY=sk-your-api-key
On Windows PowerShell:

powershell
Copy code
$env:OPENAI_API_KEY="sk-your-api-key"
Note: Ensure there are no quotes around the API key in Command Prompt. PowerShell allows quotes.

API Key Errors (e.g., 401 Unauthorized)

Cause: Invalid or incorrectly set OpenAI API key.

Solution:

Verify the API Key:

Ensure that the API key is correct and active. Log in to your OpenAI account to confirm.

Set the Environment Variable Correctly:

On Windows Command Prompt:

cmd
Copy code
set OPENAI_API_KEY=sk-your-api-key
On Windows PowerShell:

powershell
Copy code
$env:OPENAI_API_KEY="sk-your-api-key"
On Unix or MacOS:

bash
Copy code
export OPENAI_API_KEY=sk-your-api-key
Avoid Including Quotes in Command Prompt:

Do not include quotes around the API key when setting it in Command Prompt.

Test API Connectivity:

Create a simple script (test_openai.py) to verify if the API key is working:

python
Copy code
# test_openai.py

import os
from openai import OpenAI

def test_openai():
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print("Error: OpenAI API key not found.")
        return

    client = OpenAI(api_key=openai_api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a test."},
                {"role": "user", "content": "Hello, world!"}
            ],
            max_tokens=10
        )
        print("API Key is valid. Test response:", response.choices[0].message.content)
    except Exception as e:
        print(f"API Key test failed: {e}")

if __name__ == "__main__":
    test_openai()
Run the Test:

bash
Copy code
python test_openai.py
Expected Output:

If the API key is valid:

mathematica
Copy code
API Key is valid. Test response: Hello! How can I assist you today?
If invalid:

bash
Copy code
API Key test failed: Error code: 401 - {'error': {'message': "Incorrect API key provided: 'sk-your-api-key'. You can find your API key at https://platform.openai.com/account/api-keys.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}}
Permissions Issues with Log Files

Cause: The application may not have the necessary permissions to write to the logs/ directory or ai_research.log file.

Solution:

Ensure Directory Exists:

The logger.py script creates the logs/ directory if it doesn't exist. Verify that the directory exists.

Check Write Permissions:

Ensure that your user account has write permissions to the logs/ directory and ai_research.log file.

Run as Administrator:

If permissions issues persist, try running the Command Prompt or PowerShell as an administrator.

Missing Dependencies

Cause: Required Python packages are not installed.

Solution:

Install All Dependencies:

Ensure you've run:

bash
Copy code
pip install -r requirements.txt
Verify Installation:

Check if all packages are installed by listing installed packages:

bash
Copy code
pip list
Install Missing Packages Individually:

If any package is missing, install it using:

bash
Copy code
pip install package-name
Additional Troubleshooting Tips
Check Python Version:

Ensure you're using Python 3.6 or higher.

bash
Copy code
python --version
Activate Virtual Environment:

Ensure that the virtual environment is activated before running the application.

On Windows:

cmd
Copy code
venv\Scripts\activate
On Unix or MacOS:

bash
Copy code
source venv/bin/activate
Review Log Files:

Check the logs/ai_research.log file for detailed error messages and stack traces that can help identify issues.

Contributing
Contributions are welcome! If you'd like to enhance the AI Research Workflow, please follow these steps:

Fork the Repository:

Click the "Fork" button at the top right of the repository page to create a copy of the repository under your GitHub account.

Clone Your Fork:

bash
Copy code
git clone https://github.com/yourusername/ai_research_workflow.git
cd ai_research_workflow
Create a New Branch:

bash
Copy code
git checkout -b feature/your-feature-name
Make Your Changes:

Implement your enhancements, fixes, or new features.

Commit Your Changes:

bash
Copy code
git add .
git commit -m "Add feature: your feature description"
Push to Your Fork:

bash
Copy code
git push origin feature/your-feature-name
Create a Pull Request:

Navigate to your repository on GitHub and click the "Compare & pull request" button. Provide a clear description of your changes and submit the pull request.

License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software as per the license terms.

Acknowledgements
OpenAI: For providing the powerful GPT-4 language model API.
Python Community: For the vast array of libraries and tools that make development efficient and enjoyable.
You: For building and maintaining this AI Research Workflow!
Note: Replace placeholders like https://github.com/yourusername/ai_research_workflow.git with your actual repository URL and ensure that any paths or names specific to your setup are accurately reflected in the README.

Feel free to customize this README further to better fit the specific details and future enhancements of your project. If you have additional modules, tools, or instructions, consider adding them to the relevant sections.