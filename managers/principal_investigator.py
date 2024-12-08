# managers/principal_investigator.py

import logging

class PrincipalInvestigator:
    def __init__(self, name):
        """
        Initialize the Principal Investigator.

        Args:
            name (str): Name of the Principal Investigator.
        """
        self.name = name
        self.agents = []

    def add_agent(self, agent):
        """Add an AI agent to the team."""
        self.agents.append(agent)
        logging.info(f"{self.name} added {agent.name} to the team.")

    def assign_tasks(self):
        """Assign tasks to all agents and collect their results."""
        print(f"\n{self.name} is assigning tasks to AI agents...\n")
        logging.info(f"{self.name} is assigning tasks to AI agents.")
        results = []
        for agent in self.agents:
            result = agent.perform_task()
            results.append((agent.name, result))
        return results

    def review_results(self, results):
        """Review the results from all agents."""
        print("\nReviewing results...\n")
        logging.info("Reviewing results.")
        for agent_name, result in results:
            print(f"Reviewing: {result}")
            logging.info(f"Reviewed result from {agent_name}: {result}")
        print("\nAI Research Completed: All results reviewed.")
        logging.info("AI Research Completed: All results reviewed.")

    def provide_feedback(self, results):
        """
        Provide specific feedback to agents based on their results.

        Args:
            results (list): List of tuples containing agent names and their outcomes.
        """
        feedback_dict = {}
        for agent_name, outcome in results:
            if outcome == "Error detected":
                feedback_dict[agent_name] = "Address the critical error encountered in data processing."
            elif outcome == "Incomplete result":
                feedback_dict[agent_name] = "Ensure completeness and accuracy in your data analysis."
            elif outcome == "Valid result":
                feedback_dict[agent_name] = "Good job! Continue with the current strategy."
            elif outcome == "New hypothesis formed":
                feedback_dict[agent_name] = "Excellent hypothesis generation. Consider exploring additional variables."

        # Provide consolidated feedback
        for agent in self.agents:
            specific_feedback = feedback_dict.get(agent.name, "Maintain your current approach.")
            print(f"\n{self.name} is providing feedback to {agent.name}: {specific_feedback}")
            logging.info(f"{self.name} provided feedback to {agent.name}: {specific_feedback}")
            # Find the outcome for the agent
            agent_outcome = next((outcome for name, outcome in results if name == agent.name), None)
            agent.adjust_strategy(specific_feedback, error_type=agent_outcome if agent_outcome in ["Error detected", "Incomplete result"] else None)
