import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Config:
    INPUT_FILE = os.getenv("INPUT_FILE")
    OUTPUT_FILE = os.getenv("OUTPUT_FILE")
    FILE_PASSWORD = os.getenv("FILE_PASSWORD")

    @classmethod
    def log_config(cls):
        logging.info(
            f"Configuration loaded - Input FILE: {cls.INPUT_FILE}, Output FILE: {cls.OUTPUT_FILE}, Password: {'***' if cls.FILE_PASSWORD else 'None'}"
        )
