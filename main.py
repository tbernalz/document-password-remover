import argparse
from src.cli import main as cli_main
from src.gui import main as gui_main

def main():
    parser = argparse.ArgumentParser(description="Remove password from documents.")
    parser.add_argument('--cli', action='store_true', help="Run the application in CLI mode.")
    parser.add_argument('--gui', action='store_true', help="Run the application in GUI mode.")
    
    args, remaining_args = parser.parse_known_args()

    if args.cli:
        cli_main(remaining_args)
    elif args.gui:
        gui_main()
    else:
        print("Please specify a mode: --cli for Command Line Interface or --gui for Graphical User Interface.")
        parser.print_help()

if __name__ == "__main__":
    main()
