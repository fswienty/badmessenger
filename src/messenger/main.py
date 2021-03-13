import sys
import time

from .gdrive_manager import GDriveManager
from .utility_functions import print_red, print_yellow


class Messenger():
    gdrive = GDriveManager()
    user = ""

    def start(self):
        print("badmessenger start")
        self.gdrive.init()
        print_yellow(f"connected to sheet {self.gdrive.spreadsheet}")
        while self.user == "":
            print("enter your name: ", end=''),
            inp = input().strip()
            if len(inp) > 10:
                print_red("name can be at most 10 characters long")
                continue
            if len(inp) == 0:
                print_red("name cannot be empty or all whitespace")
                continue
            self.user = inp
        print_yellow("type !help or !h for a list of available commands")
        self.main_loop()

    def main_loop(self):
        while True:
            inp = input()
            if len(inp) >= 1 and inp[0] == "!":
                self.handle_commands(inp)
            elif inp == "":
                self.gdrive.fetch_messages()
            else:
                self.gdrive.write(self.user, inp)

    def handle_commands(self, cmd: str):
        cmd_sep = cmd.split()
        if cmd_sep[0] in ["!h", "!help"]:
            self.help_cmd()
        elif cmd_sep[0] in ["!r", "!rooms"]:
            self.gdrive.list_rooms()
        elif cmd_sep[0] in ["!j", "!join"]:
            if len(cmd_sep) < 2:
                print_red("missing room name")
            else:
                self.gdrive.join_room(cmd_sep[1])
        elif cmd_sep[0] in ["!f", "!fetch"]:
            if len(cmd_sep) < 2:
                print_red("missing fetch amount")
            else:
                try:
                    amount = int(cmd_sep[1])
                    self.gdrive.fetch_messages(amount)
                except Exception:
                    print_red(f"{cmd_sep[1]} is not an integer")
        elif cmd_sep[0] in ["!q", "!quit"]:
            self.quit_cmd()
        else:
            print_red("unknown command")

    def help_cmd(self):
        print_yellow("========================= HELP =========================")
        print("[!h]elp: show this help dialog")
        print("[!r]ooms: list all available rooms")
        print("[!j]oin [room]: join the room named [room]")
        print("[!f]etch [amount]: fetch the last [amount] messages")
        print("[!q]uit: quit the program")
        print("")
        print("press enter without anything typed for !fetch 20")
        print("type anything and press enter to send a message")
        print_yellow("========================================================")

    def quit_cmd(self):
        print_yellow("program quit")
        time.sleep(0.2)
        sys.exit()
