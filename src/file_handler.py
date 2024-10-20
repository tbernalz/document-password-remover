import os
from src.enum.document_types import DocumentType
from src.pdf_handler import remove_pdf_password
from src.word_handler import remove_word_password


def remove_password(input_file, output_file, password):
    ext = os.path.splitext(input_file)[1]

    try:
        document_type = DocumentType.from_extension(ext)
    except ValueError as e:
        raise ValueError(f"Unsupported file type: {ext}")

    if document_type == DocumentType.PDF:
        remove_pdf_password(input_file, output_file, password)
    elif document_type == DocumentType.WORD:
        remove_word_password(input_file, output_file, password)
    else:
        raise ValueError(f"Unsupported document type: {document_type}")
