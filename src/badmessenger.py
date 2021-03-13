from messenger.main import Messenger  # type: ignore
from colorama import init as colorama_init


if __name__ == "__main__":
    colorama_init()
    messenger = Messenger()
    messenger.start()
