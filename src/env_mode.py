import os
import logging
from src.config.config import Config
from src.pdf_handler import remove_pdf_password


def main():
    input_pdf = Config.INPUT_PDF
    output_pdf = Config.OUTPUT_PDF
    password = Config.PDF_PASSWORD

    if not input_pdf or not output_pdf:
        logging.error("Environment variables INPUT_PDF and OUTPUT_PDF are required.")
        raise ValueError("Missing required environment variables.")

    try:
        remove_pdf_password(input_pdf, output_pdf, password)
        logging.info(f"Password removed from {input_pdf} and saved to {output_pdf}")
    except Exception as e:
        logging.error(
            f"Failed to remove password using environment variables: {e}", exc_info=True
        )
        raise RuntimeError(
            f"Failed to remove password using environment variables: {e}"
        )
