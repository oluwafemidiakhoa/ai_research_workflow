# agents/ai_agent.py

import time
import random
import logging

class AIAgent:
    def __init__(self, name, expertise, task_description, max_retries=2, retry_interval=1):
        """
        Initialize an AI Agent.

        Args:
            name (str): Name of the agent.
            expertise (str): Area of expertise.
            task_description (str): Description of the task.
            max_retries (int): Maximum number of retries upon failure.
            retry_interval (int): Time in seconds between retries.
        """
        self.name = name
        self.expertise = expertise
        self.task_description = task_description
        self.max_retries = max_retries
        self.retry_interval = retry_interval
        self.retry_count = 0
        self.input_data = {}  # Placeholder for input data

    def validate_data(self):
        """Validate input data before performing the task."""
        if not self.input_data:
            logging.error(f"{self.name}: Input data is empty.")
            print(f"{self.name}: Input data is empty.")
            return False
        # Add more validation rules as needed
        return True

    def perform_task(self):
        """Perform the assigned task with retry mechanism."""
        if not self.validate_data():
            return "Error detected"

        logging.info(f"{self.name}: Starting task '{self.task_description}'.")
        print(f"{self.name} ({self.expertise}) is performing its task: {self.task_description}...")
        time.sleep(2)  # Simulate computation time

        while self.retry_count <= self.max_retries:
            result = self.generate_result()
            logging.info(f"{self.name} result: {result}")
            print(f"Result from {self.name}: {result}")

            if result in ["Valid result", "New hypothesis formed"]:
                logging.info(f"{self.name}: Task completed successfully with result '{result}'.")
                return result
            elif result == "Incomplete result":
                self.retry_count += 1
                if self.retry_count <= self.max_retries:
                    logging.warning(f"{self.name}: Incomplete result encountered. Retrying ({self.retry_count}/{self.max_retries}).")
                    print(f"{self.name} encountered an incomplete result. Retrying ({self.retry_count}/{self.max_retries})...")
                    time.sleep(self.retry_interval)  # Wait before retrying
                else:
                    logging.error(f"{self.name}: Failed after {self.max_retries} retries with outcome '{result}'.")
                    print(f"{self.name} failed after {self.max_retries} retries.")
                    return "Incomplete result"
            elif result == "Error detected":
                logging.error(f"{self.name}: Critical error encountered during task.")
                print(f"{self.name} encountered a critical error.")
                return "Error detected"

    def generate_result(self):
        """Simulate generating results (this can be refined further)."""
        return random.choice(["Valid result", "Error detected", "Incomplete result", "New hypothesis formed"])

    def adjust_strategy(self, feedback, error_type=None):
        """
        Adjust the agent's strategy based on feedback.

        Args:
            feedback (str): Feedback message.
            error_type (str, optional): Specific error type, if any.
        """
        if error_type:
            specific_feedback = f"{feedback} Specific issue: {error_type}."
        else:
            specific_feedback = feedback
        print(f"\n{self.name} is adjusting its strategy based on feedback: {specific_feedback}...")
        logging.info(f"{self.name} is adjusting strategy based on feedback: {specific_feedback}")
        self.task_description = f"Revised task based on feedback: {specific_feedback}"
        return f"{self.name} has adjusted its task based on feedback."
