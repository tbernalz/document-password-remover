import argparse
import getpass
import logging
from src.pdf_handler import remove_pdf_password


def main(remaining_args):
    parser = argparse.ArgumentParser(
        description="CLI mode: Remove password from documents"
    )
    parser.add_argument("--input", help="Path to the input PDF file")
    parser.add_argument("--output", help="Path to save the output decrypted file")
    parser.add_argument("--password", help="Password to unlock the file")

    args = parser.parse_args(remaining_args)

    input_pdf = args.input or input("Please enter the path to the input PDF file: ")
    output_pdf = args.output or input("Please enter the path to save the output file: ")
    password = args.password or getpass.getpass("Please enter the PDF password: ")

    if not input_pdf or not output_pdf or not password:
        logging.error("Missing required arguments: input, output, or password.")
        parser.print_help()
        return

    try:
        remove_pdf_password(input_pdf, output_pdf, password)
        logging.info(f"Password removed from {input_pdf} and saved to {output_pdf}")
    except Exception as e:
        logging.error(f"Failed to remove password: {e}", exc_info=True)
        raise RuntimeError(f"Failed to remove password: {e}")
