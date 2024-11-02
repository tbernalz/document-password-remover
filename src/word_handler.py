import logging
import msoffcrypto
from io import BytesIO
from docx import Document


def remove_word_password(input_word, output_word, password):
    try:
        if not output_word.lower().endswith(".docx"):
            output_word += ".docx"

        decrypted = BytesIO()

        with open(input_word, "rb") as f:
            office_file = msoffcrypto.OfficeFile(f)
            office_file.load_key(password=password)
            office_file.decrypt(decrypted)

        decrypted.seek(0)
        doc = Document(decrypted)
        doc.save(output_word)

        logging.info(f"Decrypted Word file saved to {output_word}")

    except Exception as e:
        logging.error(
            f"Failed to remove password from {input_word}: {e}", exc_info=True
        )
        raise Exception(f"Failed to remove password from {input_word}: {e}")
