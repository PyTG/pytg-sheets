import logging

from modules.pytg.ModulesLoader import ModulesLoader

from modules.sheets.SheetsManager import SheetsManager

def initialize():
    logging.info("Initializing sheets module...")

    SheetsManager.initialize()

def connect():
    sheets_manager = load_manager()

    sheets_manager.create_client()

def load_manager():
    return SheetsManager.load()

def depends_on():
    return []