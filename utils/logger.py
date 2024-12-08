# utils/logger.py

import logging
import os

def setup_logger():
    """Configure the logging settings."""
    log_directory = 'logs'
    os.makedirs(log_directory, exist_ok=True)  # Ensure the logs directory exists
    log_file = os.path.join(log_directory, 'ai_research.log')

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Also log to console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
