# managers/human_researcher.py

import logging

class HumanResearcher:
    def __init__(self, name):
        """
        Initialize the Human Researcher.

        Args:
            name (str): Name of the Human Researcher.
        """
        self.name = name

    def oversee_research(self, results):
        """Oversee the research process and handle critical issues."""
        print(f"\n{self.name} is overseeing the research process...")
        logging.info(f"{self.name} is overseeing the research process.")
        error_messages = []
        for result in results:
            agent_name, outcome = result
            if outcome in ["Error detected", "Incomplete result"]:
                error_messages.append(f"{agent_name}: {outcome}")
                logging.warning(f"{agent_name} encountered an issue: {outcome}")

        if error_messages:
            # Consolidate all error messages into a single alert
            alert_message = "Alert! The following results require human intervention:\n" + "\n".join(error_messages)
            print(alert_message)
            logging.warning(f"Human intervention required:\n{alert_message}")
        else:
            print("All tasks completed successfully.")
            logging.info("All tasks completed successfully.")
        print("Human review complete. Proceeding to final conclusions.")
        logging.info("Human review complete. Proceeding to final conclusions.")
