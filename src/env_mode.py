import os
import logging
from src.config.config import Config
from src.file_handler import remove_password


def main():
    input_file = Config.INPUT_FILE
    output_file = Config.OUTPUT_FILE
    password = Config.FILE_PASSWORD

    if not input_file or not output_file:
        logging.error("Environment variables INPUT_FILE and OUTPUT_FILE are required.")
        raise ValueError("Missing required environment variables.")

    try:
        remove_password(input_file, output_file, password)
        logging.info(f"Password removed from {input_file} and saved to {output_file}")
    except Exception as e:
        logging.error(
            f"Failed to remove password using environment variables: {e}", exc_info=True
        )
        raise RuntimeError(
            f"Failed to remove password using environment variables: {e}"
        )
