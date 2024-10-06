from PyPDF2 import PdfReader, PdfWriter
from dotenv import load_dotenv
import os

load_dotenv()

def remove_pdf_password(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    reader.decrypt(password)

    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

input_pdf = os.getenv('INPUT_PDF')
output_pdf = os.getenv('OUTPUT_PDF')
password = os.getenv('PDF_PASSWORD')

remove_pdf_password(input_pdf, output_pdf, password)
