import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Config:
    INPUT_PDF = os.getenv("INPUT_PDF")
    OUTPUT_PDF = os.getenv("OUTPUT_PDF")
    PDF_PASSWORD = os.getenv("PDF_PASSWORD")

    @classmethod
    def log_config(cls):
        logging.info(
            f"Input PDF: {cls.INPUT_PDF}, Output PDF: {cls.OUTPUT_PDF}, Password: {cls.PDF_PASSWORD}"
        )
