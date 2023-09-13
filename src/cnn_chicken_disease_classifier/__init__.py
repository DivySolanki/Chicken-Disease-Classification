import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Sends logging output to a disk file
        logging.StreamHandler(sys.stdout),  # Prints the logs in console
    ],
)

logger = logging.getLogger(
    "cnnClassifierLogger"
)  # Creates a log for specified file name
