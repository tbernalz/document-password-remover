from config.config import Config
from src.pdf_handler import remove_pdf_password

def main(args):
    input_pdf = args.pdf or Config.INPUT_PDF
    output_pdf = args.output or Config.OUTPUT_PDF
    password = args.password or Config.PDF_PASSWORD

    if not input_pdf or not output_pdf or not password:
        print("Error: Input PDF, output PDF, and password must be provided either via arguments or environment variables")
        return

    try:
        remove_pdf_password(input_pdf, output_pdf, password)
        print(f"Password removed from {input_pdf} and saved to {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")
