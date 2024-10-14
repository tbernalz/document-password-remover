from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_password(input_pdf, output_pdf, password):
    try:
        if not output_pdf.lower().endswith('.pdf'):
            output_pdf += '.pdf'

        reader = PdfReader(input_pdf)
        if reader.is_encrypted:
            reader.decrypt(password)
        else:
            print(f"Warning: {input_pdf} is not encrypted")
        
        writer = PdfWriter()
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

    except Exception as e:
        print(f"Error: Failed to remove password from {input_pdf}: {e}")
        raise Exception(f"Failed to remove password from {input_pdf}: {e}")
