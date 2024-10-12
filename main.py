import argparse
from src.cli import main as cli_main

def main():    
    parser = argparse.ArgumentParser(description="Remove password from documents.")
    parser.add_argument('--pdf', help="Path to the input PDF file")
    parser.add_argument('--output', help="Path to save the output decrypted file")
    parser.add_argument('--password', help="Password to unlock the file")
    
    args = parser.parse_args()

    cli_main(args)

if __name__ == "__main__":
    main()
