import tkinter as tk
import logging
from tkinter import filedialog, messagebox

from src.file_handler import remove_password
from src.enum.document_types import DocumentType


def main():
    root = tk.Tk()
    root.title("Document Password Remover")

    def select_input_file():
        selected_type = document_type_var.get().lower()
        file_types = [(f"{selected_type.upper()} Files", f"*.{selected_type}")]
        input_file = filedialog.askopenfilename(
            title=f"Select {selected_type.upper()} File", filetypes=file_types
        )
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, input_file)
        logging.info(f"Input {selected_type.upper()} selected: {input_file}")

    def select_output_file():
        selected_type = document_type_var.get().lower()
        output_file = filedialog.asksaveasfilename(
            title=f"Save Decrypted {selected_type.upper()} As",
            defaultextension=f".{selected_type}",
            filetypes=[(f"{selected_type.upper()} Files", f"*.{selected_type}")],
        )
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, output_file)
        logging.info(f"Output {selected_type.upper()} selected: {output_file}")

    def decrypt_document():
        input_file = input_file_entry.get()
        output_file = output_file_entry.get()
        password = password_entry.get()
        document_type = document_type_var.get().lower()

        if not input_file or not output_file or not password:
            messagebox.showerror(
                "Error",
                "All fields (Input Path, Output Path, and Password) must be provided.",
            )
            logging.error("Error: Missing required fields.")
            return

        try:
            remove_password(input_file, output_file, password)
            logging.info(
                f"Success: Password removed from {input_file} and saved as {output_file}"
            )
            messagebox.showinfo(
                "Success",
                f"Password removed from {input_file} and saved as {output_file}.",
            )
        except Exception as e:
            logging.error(
                f"Error: Failed to remove password from {input_file}: {e}",
                exc_info=True,
            )
            messagebox.showerror("Error", f"Failed to remove password: {e}")

    document_type_label = tk.Label(root, text="Document Type:")
    document_type_label.grid(row=0, column=0, padx=10, pady=5)

    document_type_var = tk.StringVar(root)
    document_type_var.set(DocumentType.PDF.value)

    document_type_dropdown = tk.OptionMenu(
        root, document_type_var, *[doc.value.upper() for doc in DocumentType]
    )
    document_type_dropdown.grid(row=0, column=1, padx=10, pady=5)

    input_file_label = tk.Label(root, text="Input File:")
    input_file_label.grid(row=1, column=0, padx=10, pady=5)

    input_file_entry = tk.Entry(root, width=40)
    input_file_entry.grid(row=1, column=1, padx=10, pady=5)

    input_file_button = tk.Button(root, text="Browse...", command=select_input_file)

    input_file_button.grid(row=1, column=2, padx=10, pady=5)

    output_file_label = tk.Label(root, text="Output File:")
    output_file_label.grid(row=2, column=0, padx=10, pady=5)

    output_file_entry = tk.Entry(root, width=40)
    output_file_entry.grid(row=2, column=1, padx=10, pady=5)

    output_file_button = tk.Button(root, text="Browse...", command=select_output_file)
    output_file_button.grid(row=2, column=2, padx=10, pady=5)

    password_label = tk.Label(root, text="Password:")
    password_label.grid(row=3, column=0, padx=10, pady=5)

    password_entry = tk.Entry(root, show="*", width=40)
    password_entry.grid(row=3, column=1, padx=10, pady=5)

    decrypt_button = tk.Button(root, text="Remove Password", command=decrypt_document)
    decrypt_button.grid(row=4, columnspan=3, pady=10)

    root.mainloop()
