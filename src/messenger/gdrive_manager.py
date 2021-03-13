# import google api library
import gspread
from gspread.models import Worksheet
# Service client credential from oauth2client
from oauth2client.service_account import ServiceAccountCredentials

import time
from datetime import datetime
from colorama import Fore

from .utility_functions import get_path, print_red, utc_to_local, print_yellow


class GDriveManager():
    client = None
    spreadsheet = None
    msg_sheet = None

    last_fetch_time = ""

    def init(self):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://www.googleapis.com/auth/analytics.readonly',
                 'https://www.googleapis.com/auth/drive',
                 'https://www.googleapis.com/auth/spreadsheets']
        # create some credential using that scope and content of startup_funding.json
        creds = ServiceAccountCredentials.from_json_keyfile_name(get_path('client_credentials.json'), scope)
        # create gspread authorize using that credential
        self.client = gspread.authorize(creds)
        # Find a spreadsheet by name
        self.spreadsheet = self.client.open("BadMessenger")

    def list_rooms(self):
        rooms = self.spreadsheet.worksheets()
        print_yellow("====== AVAILABLE ROOMS ======")
        for i in range(0, len(rooms)):
            print(rooms[i].title)

        print_yellow("=============================")

    def join_room(self, room: str):
        try:
            self.msg_sheet = self.spreadsheet.worksheet(room)
            print_yellow(f"entered room {room}")
            self.last_fetch_time = -999
            self.fetch_messages()
        except Exception:
            print_red(f"room {room} does not exist")

    def write(self, user: str, msg: str):
        # check if user is an a room
        if type(self.msg_sheet) != Worksheet:
            print_red("please enter a room")
            return
        # append message to the end of the sheet
        self.msg_sheet.append_row([str(datetime.utcnow()), user, msg])

    def fetch_messages(self, amount: int = 20):
        # check if user is an a room
        if type(self.msg_sheet) != Worksheet:
            print_red("please enter a room")
            return
        # check if the fetch cooldown is over
        fetch_cooldown = 3 - (time.time() - self.last_fetch_time)
        if fetch_cooldown > 0:
            print_red(f"please wait {str(fetch_cooldown)[0:3]} sec before fetching again")
            return
        # get messages from server
        print_yellow(f"======================== LAST {amount} MESSAGES ========================")
        messages = self.msg_sheet.get_all_values()
        # check if room has messages
        if len(messages) == 0:
            print_red("no messages")
        # check if old messages need to be deleted
        if len(messages) > 200:
            self.reset(messages)
        # print messages
        min_range = max(0, len(messages) - amount)
        for i in range(min_range, len(messages)):
            msg = messages[i]
            local_time = utc_to_local(msg[0])
            user_appended = f"{msg[1]}:".ljust(11)
            # print(local_time[11:16], end='')
            # print("  ", end='')
            # print_cyan(user_appended, end='')
            # print(" ", end='')
            # print(msg[2])
            print(Fore.MAGENTA + local_time[11:16] + Fore.CYAN + "  " + user_appended + " " + Fore.RESET + msg[2])
        print_yellow("==================================================================")
        # set fetch time for the cooldown
        self.last_fetch_time = time.time()

    def reset(self, messages: list):
        self.msg_sheet.clear()
        self.msg_sheet.append_rows(messages[-100:])
