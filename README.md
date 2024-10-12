# Document Password Remover

This project is a tool for removing passwords from PDF files. The application allows you to provide the input PDF, output PDF, and password through environment variables or command-line arguments via a CLI interface.

## 🚀 Features

- Remove passwords from encrypted PDF files.

- Provide input and output paths through environment variables or command-line arguments.

- Modular structure for easier maintenance and enhancements.

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

Run the program in CLI mode by directly providing the required values:

```bash
python main.py --pdf path/to/input.pdf --output path/to/output.pdf --password your_pdf_password
```

### Environment Variables Mode

Ensure the .env file is set up correctly, and then run the script:

```bash
python main.py
```

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
│   └── pdf_handler.py          # Functions for handling PDF decryption
│
├── .env                        # Environment variables file
├── .env.example                # Example file showing required environment variables
├── .gitignore                  # Specifies files and directories to be ignored by Git
├── main.py                     # Main entry point of the application, orchestrates PDF password removal via CLI
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
