# main.py

import os
import re
import logging
from agents.ai_agent import AIAgent
from agents.hypothesis_agent import HypothesisAgent
from utils.logger import setup_logger
from managers.principal_investigator import PrincipalInvestigator
from managers.human_researcher import HumanResearcher
from openai import OpenAI

def run_research_process():
    """Execute the full AI research workflow."""
    # Setup logger
    setup_logger()
    logging.info("Starting AI Research Workflow.")

    print("\nDr. James Zou is assigning tasks to AI agents...\n")

    # Initialize OpenAI client
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        logging.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        print("Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        return

    client = OpenAI(api_key=openai_api_key)

    # Initialize Principal Investigator
    pi = PrincipalInvestigator("Dr. James Zou")

    # Define agents with tailored retry configurations
    agent_immunology = AIAgent(
        name="Immunology AI",
        expertise="Immunology",
        task_description="Designing nanobodies for SARS-CoV-2",
        max_retries=1,
        retry_interval=1
    )
    agent_bioinformatics = AIAgent(
        name="Bioinformatics AI",
        expertise="Computational Biology",
        task_description="Analyzing gene sequences for antiviral response",
        max_retries=2,
        retry_interval=1
    )
    agent_ml = AIAgent(
        name="ML AI",
        expertise="Machine Learning",
        task_description="Building predictive models for drug efficacy",
        max_retries=1,
        retry_interval=1
    )
    hypothesis_agent = HypothesisAgent(
        name="Hypothesis Generator",
        expertise="Hypothesis Generation",
        client=client,
        max_retries=2,
        retry_interval=1
    )

    # Add agents to the team
    pi.add_agent(agent_immunology)
    pi.add_agent(agent_bioinformatics)
    pi.add_agent(agent_ml)
    pi.add_agent(hypothesis_agent)

    # Provide input data (example)
    agent_immunology.input_data = {"nanobody_sequences": ["SEQ123", "SEQ456"]}
    agent_bioinformatics.input_data = {"gene_sequences": ["GENE1", "GENE2"]}
    agent_ml.input_data = {"drug_efficacy_data": {"drug1": 0.8, "drug2": 0.6}}
    hypothesis_agent.input_data = {"literature_data": ["Study A", "Study B"]}

    # Perform research tasks
    results = pi.assign_tasks()

    # Review results and handle errors gracefully
    pi.review_results(results)

    # Provide feedback and adjust strategies
    pi.provide_feedback(results)

    # Generate the new hypothesis
    new_hypothesis = hypothesis_agent.generate_hypothesis()

    # Human oversight
    human_researcher = HumanResearcher("Nyah Aduke")
    human_researcher.oversee_research(results)

    # Final summary
    print("\n--- Final Overview ---")
    logging.info("Final overview: AI agents have refined their strategies, and the hypothesis has been adjusted.")
    print(f"AI agents have refined their strategies, and the hypothesis has been adjusted.")

    # Remove redundant "Hypothesis: " in the final display if it still exists
    new_hypothesis = re.sub(r'^Hypothesis:\s*', '', new_hypothesis, flags=re.IGNORECASE).strip()
    print(f"Generated Hypothesis: {new_hypothesis}")
    logging.info(f"Generated Hypothesis: {new_hypothesis}")
    print(f"The human researcher has ensured the research is on track.")
    logging.info("The human researcher has ensured the research is on track.")

    logging.info("AI Research Workflow completed successfully.")

# Run the full research process
if __name__ == "__main__":
    run_research_process()
