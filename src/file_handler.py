import os
from src.enum.file_types import FileType
from src.pdf_handler import remove_pdf_password
from src.word_handler import remove_word_password
from src.excel_handler import remove_excel_password


def remove_password(input_file, output_file, password):
    ext = os.path.splitext(input_file)[1]

    try:
        file_type = FileType.from_extension(ext)
    except ValueError as e:
        raise ValueError(f"Unsupported file type: {ext}")

    if file_type == FileType.PDF:
        remove_pdf_password(input_file, output_file, password)
    elif file_type == FileType.WORD:
        remove_word_password(input_file, output_file, password)
    elif file_type == FileType.EXCEL:
        remove_excel_password(input_file, output_file, password)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")
