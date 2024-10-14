# Document Password Remover

This project is a tool for removing passwords from PDF files. The application allows you to provide the input PDF, output PDF, and password through environment variables or both a **command-line interface (CLI)** and an optional **graphical user interface (GUI)**, allowing users to easily remove passwords and save the decrypted versions of their documents.

## 🚀 Features

- Remove passwords from encrypted PDF files.

- Multiple Interfaces: Use either the command-line interface (CLI) or the graphical user interface (GUI).

- Modular Design: Easily extensible for future development or new file types.

## 📦 Setup and Installation

### Requirements

Before starting, make sure you have the following installed:

- Python 3.7+
- pip (Python package installer)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/tbernalz/document-password-remover.git
    cd document-password-remover
    ```

1.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

1.  Create the .env file for configuration (or use CLI):

    Edit the .env file with your paths:

    ```bash
    INPUT_PDF=path/to/input.pdf
    OUTPUT_PDF=path/to/output.pdf
    PDF_PASSWORD=your_pdf_password
    ```

## 🚸 Usage

### CLI Mode

Run the program in CLI mode by using the --cli flag. You can provide file paths and passwords through command-line arguments.

```bash
python main.py --cli --input path/to/input.pdf --output path/to/output.pdf --password your_pdf_password
```

### GUI Mode

To run the program in GUI mode, use the --gui flag:

```bash
python main.py --gui
```

In GUI mode, a simple interface will allow you to browse for files and input passwords.

### Environment Variables Mode

Ensure the .env file is set up correctly, and then run the script:

```bash
python main.py --cli
```

Note that in the Environment Variables Mode, you only need to add the `--cli`, but not the rest of flags.

## project directory tree:

```bash
document-password-remover/
│
├── src/
│   ├── __init__.py             # Marks src as a package
│   ├── config/
│   │   ├── __init__.py         # Marks config as a package
│   │   └── config.py           # Configuration handling
│   ├── cli.py                  # Command-line interface implementation
│   ├── gui.py                  # Optional GUI implementation (using Tkinter)
│   └── pdf_handler.py          # Functions for handling PDF decryption
│
├── .env                        # Environment variables file
├── .env.example                # Example file showing required environment variables
├── .gitignore                  # Specifies files and directories to be ignored by Git
├── main.py                     # Main entry point of the application, orchestrates PDF password removal via CLI or GUI
├── README.md                   # Main project documentation
└── requirements.txt            # Dependencies required to run the project

```

## 🌟 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## ✉️ Contact

Tomás Bernal Zuluaga - [tbernalz@eafit.edu.co](mailto:tbernalz@eafit.edu.co)

<a href="https://www.linkedin.com/in/tbernalz" target="_blank" rel="noreferrer">
    <img src="https://seeklogo.com/images/L/linkedin-new-2020-logo-E14A5D55ED-seeklogo.com.png" alt="Linkedin" width="40" height="40"/>
</a>
