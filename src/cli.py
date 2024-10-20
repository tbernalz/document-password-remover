import argparse
import getpass
import logging

from src.file_handler import remove_password
from src.enum.document_types import DocumentType


def main(remaining_args):
    parser = argparse.ArgumentParser(
        description="CLI mode: Remove password from documents"
    )
    parser.add_argument(
        "--document",
        help=f"Document type to remove password from. Supported types: {', '.join([doc.value for doc in DocumentType])}",
    )
    parser.add_argument("--input", help="Path to the input file")
    parser.add_argument("--output", help="Path to save the output decrypted file")
    parser.add_argument("--password", help="Password to unlock the file")

    args = parser.parse_args(remaining_args)

    available_docs = ", ".join([doc.value for doc in DocumentType])
    document = (
        args.document
        or input(f"Please enter the document type ({available_docs}): ").lower()
    )

    try:
        document_type = DocumentType(document)
    except ValueError:
        logging.error(
            f"Unsupported document type: {document}. Supported types: {available_docs}"
        )
        return
    input_file = args.input or input(
        f"Please enter the path to the input {document} file: "
    )
    output_file = args.output or input(
        "Please enter the path to save the output file: "
    )
    password = args.password or getpass.getpass(
        f"Please enter the {document} password: "
    )

    if not input_file or not output_file or not password:
        logging.error("Missing required arguments: input, output, or password.")
        parser.print_help()
        return

    try:
        remove_password(input_file, output_file, password)
        logging.info(f"Password removed from {input_file} and saved to {output_file}")
    except Exception as e:
        logging.error(f"Failed to remove password: {e}", exc_info=True)
        raise RuntimeError(f"Failed to remove password: {e}")
