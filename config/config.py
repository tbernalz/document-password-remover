import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    INPUT_PDF = os.getenv('INPUT_PDF')
    OUTPUT_PDF = os.getenv('OUTPUT_PDF')
    PDF_PASSWORD = os.getenv('PDF_PASSWORD')
