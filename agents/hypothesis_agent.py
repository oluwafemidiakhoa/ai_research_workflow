# agents/hypothesis_agent.py

import re
import logging
from openai import OpenAI

from .ai_agent import AIAgent

class HypothesisAgent(AIAgent):
    def __init__(self, name, expertise, client, max_retries=2, retry_interval=1):
        """
        Initialize the Hypothesis Agent.

        Args:
            name (str): Name of the agent.
            expertise (str): Area of expertise.
            client (OpenAI): OpenAI client instance.
            max_retries (int): Maximum number of retries upon failure.
            retry_interval (int): Time in seconds between retries.
        """
        super().__init__(name, expertise, "Generating new hypotheses based on scientific data", max_retries, retry_interval)
        self.client = client  # OpenAI client

    def generate_hypothesis(self):
        """Generate a hypothesis autonomously based on literature and data."""
        print(f"\n{self.name} is generating a new hypothesis based on data from literature...")
        logging.info(f"{self.name} is generating a new hypothesis.")

        try:
            # Refine the prompt to instruct the AI not to include the "Hypothesis:" prefix
            response = self.client.chat.completions.create(
                model="gpt-4",  # Using GPT-4 (chat-based model)
                messages=[
                    {"role": "system", "content": "You are an AI research assistant."},
                    {"role": "user", "content": "Generate a hypothesis on the latest breakthroughs in AI-driven drug discovery without including the prefix 'Hypothesis:' in your response."}
                ],
                max_tokens=200
            )

            # Access the response and ensure no redundant prefix
            hypothesis = response.choices[0].message.content.strip()

            # Remove any leading "Hypothesis:" if it exists, using regex for robustness
            hypothesis = re.sub(r'^Hypothesis:\s*', '', hypothesis, flags=re.IGNORECASE)

            logging.info(f"Generated hypothesis: {hypothesis}")
            print(f"Generated Hypothesis: {hypothesis}")
            return hypothesis
        except Exception as e:
            error_message = f"Error detected during hypothesis generation: {e}"
            logging.error(error_message)
            print(error_message)
            return "Error detected"
