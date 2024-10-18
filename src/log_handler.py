import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(log_file, max_bytes=5000000, backup_count=5):
    """
    Sets up logging configuration, logs to both a file and the console.

    Parameters:
    log_file (str): The file where logs will be saved.
    max_bytes (int): The maximum size (in bytes) for the log file before rotation occurs. Default is 5MB.
    backup_count (int): The number of rotated log files to keep. Default is 5.
    """

    # Ensure the directory for log file exists
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))

    # Check if logging is already configured
    if not logging.getLogger().hasHandlers():
        # File handler with rotating logs
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        # Console handler for real-time logging to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)

        # Set up the root logger with the specified handlers
        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[file_handler, console_handler],
            force=True,  # Force reconfiguration if logging was already set up
        )

    logging.info("Logging setup complete.")


if __name__ == "__main__":
    # Example of how to set up logging
    setup_logging(log_file="logs/app.log")
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")
