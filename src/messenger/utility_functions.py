import time
from colorama import Fore
from datetime import datetime
from pathlib import Path


def get_path(relative_path: str) -> str:
    return Path(__file__).parent.absolute().joinpath(relative_path)


def utc_to_local(utc_datetime_str: str) -> str:
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return str(datetime.fromisoformat(utc_datetime_str) + offset)


def print_red(text: str):
    print(Fore.RED + text + Fore.RESET)


# def print_cyan(text: str, **kwargs):
#     print(Fore.CYAN + text + Fore.RESET, kwargs)


def print_yellow(text: str):
    print(Fore.YELLOW + text + Fore.RESET)
