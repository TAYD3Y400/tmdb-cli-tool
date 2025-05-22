import argparse
from tmdb_cli_tool.tmdb import get_now_playing, get_popular, get_top_rated, get_upcoming

def main() -> None:
    """main function to create the cli and call the fetch function by category"""
    parser = argparse.ArgumentParser(
        prog="tmdb-cli-tool",
        description="TMDB CLI tool")

    subparsers = parser.add_subparsers(dest="command", help="sub-command help")

    type_parser = subparsers.add_parser("type", help="Type help")

    type_parser.add_argument("category", type=str,
                             help="Category",
                             choices=["playing", "popular", "top", "upcoming"])

    args = parser.parse_args()

    # Link the functions with the list of choices
    commands = {
        "playing": get_now_playing,
        "popular": get_popular,
        "top": get_top_rated,
        "upcoming": get_upcoming,
    }

    # Call the respective function
    if args.command == "type":
        command_function = commands.get(args.category)
        if command_function:
            command_function()
    else:
        parser.print_help()
