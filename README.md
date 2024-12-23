# File Password Remover

This project is a tool for removing passwords from different types of files, including PDF, Excel and Word files. The application allows you to provide the input file, output file, and password through environment variables or both a **command-line interface (CLI)** and an optional **graphical user interface (GUI)**, allowing users to easily remove passwords and save the decrypted versions of their files.

## 🚀 Features

- Support for PDF, Excel and Word files: Remove passwords and save decrypted copies.

- Multiple Interfaces: Use either the command-line interface (CLI), graphical user interface (GUI), or environment variables mode.

- Modular Design: Easily extensible for future development or new file types.

- Logging: Logs all actions for debugging and future reference.

## 📦 Setup and Installation

### Requirements

Before starting, make sure you have the following installed:

- Python 3.7+
- pip (Python package installer)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/tbernalz/file-password-remover.git
    cd file-password-remover
    ```

1.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

1.  Optionally, create the `.env` file for configuration (for Environment Variables mode):

    Edit the `.env` file with your paths:

    ```bash
    INPUT_FILE=path/to/input.file
    OUTPUT_FILE=path/to/output.file
    FILE_PASSWORD=your_file_password
    ```

## 🚸 Usage

### CLI Mode

Run the program in CLI mode by using the `--cli` flag. You can provide file paths and passwords through command-line arguments or use the interactive mode to input them.

#### **1. Non-Interactive CLI Mode (with arguments)**

In this mode, you provide all the necessary information as command-line arguments:

```bash
python main.py --cli --input path/to/input.file --output path/to/output.file --password your_file_password
```

This is ideal for automating processes and scripting.

#### **2. Interactive CLI Mode**

In the interactive mode, you don't need to pass the input arguments directly. Instead, the program will prompt you to enter the required information interactively during runtime.

```bash
python main.py --cli
```

Example of how it works:

```bash
(program) Please enter the input path:
(user) path/to/input.file
(program) Please enter the output path:
(user) path/to/output.file
(program) Please enter the password:
(user) your_file_password
```

This mode is ideal for users who prefer a more guided experience (it hides the password when typed).

### GUI Mode

To run the program in GUI mode, use the `--gui` flag:

```bash
python main.py --gui
```

In GUI mode, a simple interface will allow you to browse for files and input passwords.

### Environment Variables Mode

If you prefer to configure everything through environment variables, you can use this mode. Ensure the .env file is set up correctly, and then run the script:

```bash
python main.py
```

(You can run `python main.py --help` to see the help usage message)

## 📂 Project directory tree:

```bash
file-password-remover/
│
├── logs/
│   └── app.log                 # Log file where application logs are written
│
├── src/
│   ├── __init__.py             # Marks src as a package
│   ├── config/
│   │   ├── __init__.py         # Marks config as a package
│   │   └── config.py           # Configuration handling (e.g., loading .env variables)
│   ├── cli.py                  # Command-line interface implementation
│   ├── gui.py                  # GUI implementation (using Tkinter)
│   ├── env_mode.py             # Environment variables mode implementation
│   ├── excel_handler.py        # Functions for handling Excel decryption
│   ├── log_handler.py          # Log setup file for logging to app.log and console
│   ├── pdf_handler.py          # Functions for handling PDF decryption
│   └── word_handler.py         # Functions for handling Word decryption
│
├── .env                        # Environment variables file
├── .env.example                # Example file showing required environment variables
├── .gitignore                  # Specifies files and directories to be ignored by Git
├── main.py                     # Main entry point of the application, orchestrates file password removal via CLI, GUI, or Env Mode
├── README.md                   # Main project documentation
├── requirements.txt            # Dependencies required to run the project
└── setup.py                    # Setup script for packaging the project
```

## 🌟 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## ✉️ Contact

Tomás Bernal Zuluaga - [tbernalz@eafit.edu.co](mailto:tbernalz@eafit.edu.co)

<a href="https://www.linkedin.com/in/tbernalz" target="_blank" rel="noreferrer">
    <img src="https://seeklogo.com/images/L/linkedin-new-2020-logo-E14A5D55ED-seeklogo.com.png" alt="Linkedin" width="40" height="40"/>
</a>
