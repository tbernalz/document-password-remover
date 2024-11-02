import os
import argparse
import logging

from src.cli import main as cli_main
from src.gui import main as gui_main
from src.log_handler import setup_logging
from src.env_mode import main as env_mode_main


def main():
    setup_logging(log_file="logs/app.log")

    parser = argparse.ArgumentParser(description="Remove password from files.")
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
        try:
            env_mode_main()
        except Exception as e:
            logging.error(
                f"Failed to run in environment variables mode: {e}", exc_info=True
            )
            print(
                "No mode specified. Use --cli for CLI mode, --gui for GUI mode, or set the appropriate environment variables."
            )
            parser.print_help()


if __name__ == "__main__":
    main()
