import logging
from PyPDF2 import PdfReader, PdfWriter


def remove_pdf_password(input_pdf, output_pdf, password):
    try:
        if not output_pdf.lower().endswith(".pdf"):
            output_pdf += ".pdf"

        reader = PdfReader(input_pdf)
        if reader.is_encrypted:
            reader.decrypt(password)
            logging.info(f"Successfully decrypted {input_pdf}")
        else:
            logging.warning(f"{input_pdf} is not encrypted")

        writer = PdfWriter()
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
            logging.info(f"Decrypted PDF saved to {output_pdf}")

    except Exception as e:
        logging.error(f"Failed to remove password from {input_pdf}: {e}", exc_info=True)
        raise Exception(f"Failed to remove password from {input_pdf}: {e}")
