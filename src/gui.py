import tkinter as tk
import logging
from tkinter import filedialog, messagebox

from src.pdf_handler import remove_pdf_password


def main():
    root = tk.Tk()
    root.title("Document Password Remover")

    def select_input_file():
        input_file = filedialog.askopenfilename(title="Select PDF File")
        input_pdf_entry.delete(0, tk.END)
        input_pdf_entry.insert(0, input_file)
        logging.info(f"Input PDF selected: {input_file}")

    def select_output_file():
        output_file = filedialog.asksaveasfilename(
            title="Save Decrypted PDF As", defaultextension=".pdf"
        )
        output_pdf_entry.delete(0, tk.END)
        output_pdf_entry.insert(0, output_file)
        logging.info(f"Output PDF selected: {output_file}")

    def decrypt_pdf():
        input_pdf = input_pdf_entry.get()
        output_pdf = output_pdf_entry.get()
        password = password_entry.get()

        if not input_pdf or not output_pdf or not password:
            messagebox.showerror(
                "Error",
                "All fields (Input Path, Output Path, and Password) must be provided.",
            )
            logging.error("Error: Missing required fields.")
            return

        try:
            remove_pdf_password(input_pdf, output_pdf, password)
            logging.info(
                f"Success: Password removed from {input_pdf} and saved as {output_pdf}"
            )
            messagebox.showinfo(
                "Success",
                f"Password removed from {input_pdf} and saved as {output_pdf}.",
            )
        except Exception as e:
            logging.error(
                f"Error: Failed to remove password from {input_pdf}: {e}", exc_info=True
            )
            messagebox.showerror("Error", f"Failed to remove password: {e}")

    input_pdf_label = tk.Label(root, text="Input PDF:")
    input_pdf_label.grid(row=0, column=0, padx=10, pady=5)

    input_pdf_entry = tk.Entry(root, width=40)
    input_pdf_entry.grid(row=0, column=1, padx=10, pady=5)

    input_pdf_button = tk.Button(root, text="Browse...", command=select_input_file)
    input_pdf_button.grid(row=0, column=2, padx=10, pady=5)

    output_pdf_label = tk.Label(root, text="Output PDF:")
    output_pdf_label.grid(row=1, column=0, padx=10, pady=5)

    output_pdf_entry = tk.Entry(root, width=40)
    output_pdf_entry.grid(row=1, column=1, padx=10, pady=5)

    output_pdf_button = tk.Button(root, text="Browse...", command=select_output_file)
    output_pdf_button.grid(row=1, column=2, padx=10, pady=5)

    password_label = tk.Label(root, text="Password:")
    password_label.grid(row=2, column=0, padx=10, pady=5)

    password_entry = tk.Entry(root, show="*", width=40)
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    decrypt_button = tk.Button(root, text="Remove Password", command=decrypt_pdf)
    decrypt_button.grid(row=3, columnspan=3, pady=10)

    root.mainloop()
