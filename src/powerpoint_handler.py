import logging
import msoffcrypto
from pptx import Presentation
import io


def remove_powerpoint_password(input_pptx, output_pptx, password):
    try:
        if not output_pptx.lower().endswith(".pptx"):
            output_pptx += ".pptx"

        decrypted_pptx = io.BytesIO()
        with open(input_pptx, "rb") as file:
            office_file = msoffcrypto.OfficeFile(file)
            office_file.load_key(password=password)

            office_file.decrypt(decrypted_pptx)

        decrypted_pptx.seek(0)
        prs = Presentation(decrypted_pptx)

        prs.save(output_pptx)

        logging.info(f"Successfully decrypted {input_pptx} and saved to {output_pptx}")

    except Exception as e:
        logging.error(
            f"Failed to remove password from {input_pptx}: {e}", exc_info=True
        )
        raise Exception(f"Failed to remove password from {input_pptx}: {e}")
