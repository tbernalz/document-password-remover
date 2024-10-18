import argparse
import logging
from src.cli import main as cli_main
from src.gui import main as gui_main
from src.log_handler import setup_logging


def main():
    setup_logging(log_file="logs/app.log")

    parser = argparse.ArgumentParser(description="Remove password from documents.")
    parser.add_argument(
        "--cli", action="store_true", help="Run the application in CLI mode."
    )
    parser.add_argument(
        "--gui", action="store_true", help="Run the application in GUI mode."
    )

    args, remaining_args = parser.parse_known_args()

    if args.cli:
        try:
            cli_main(remaining_args)
        except Exception as e:
            logging.error(f"CLI mode failed with error: {e}", exc_info=True)
    elif args.gui:
        try:
            gui_main()
        except Exception as e:
            logging.error(f"GUI mode failed with error: {e}", exc_info=True)

    else:
        logging.error(
            "No mode specified. Use --cli for CLI mode or --gui for GUI mode."
        )
        parser.print_help()


if __name__ == "__main__":
    main()
