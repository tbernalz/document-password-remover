import io
import logging
import msoffcrypto
from openpyxl import load_workbook


def remove_excel_password(input_excel, output_excel, password):
    try:
        if not output_excel.lower().endswith(".xlsx"):
            output_excel += ".xlsx"

        decrypted_stream = io.BytesIO()
        with open(input_excel, "rb") as f_in:
            office_file = msoffcrypto.OfficeFile(f_in)
            office_file.load_key(password=password)
            office_file.decrypt(decrypted_stream)

        decrypted_stream.seek(0)
        wb = load_workbook(filename=decrypted_stream)
        wb.security = None
        wb.save(output_excel)

        logging.info(
            f"Successfully decrypted {input_excel} and saved to {output_excel}"
        )

    except Exception as e:
        logging.error(
            f"Failed to remove password from {input_excel}: {e}", exc_info=True
        )
        raise Exception(f"Failed to remove password from {input_excel}: {e}")
