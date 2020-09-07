import gspread, traceback, logging

from time import sleep

import urllib.request

from modules.pytg.Manager import Manager
from modules.pytg.load import get_module_content_folder

class SheetsManager(Manager):
    @staticmethod
    def initialize():
        SheetsManager.__instance = SheetsManager()

        return

    @staticmethod
    def load():
        return SheetsManager.__instance

    def __init__(self):
        self.client = None

    def create_client(self, credentials_id = "credentials"):
        self.client = gspread.service_account(filename='{}/{}.json'.format(get_module_content_folder("sheets"), credentials_id))

    def connect(self):
        return self.client

    def safe_request(self, func, args, max_tries = 3):
        done = False
        tries = 1

        ret_value = None

        while not done and tries < max_tries:
            try: 
                ret_value = func(*args)

                done = True
            except:
                logging.warning("Exception on request {} with args {} (try {}/{})".format(func, args, tries, max_tries))

                traceback.print_exc()

                tries += 1

                sleep(30)

                self.create_client()

        return ret_value
        