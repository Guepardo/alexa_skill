from .open_chrome import OpenChrome


class Locator:
    COMMAND_LIST = {
        "1": OpenChrome
    }

    def find(self, command_number: str):
        return self.COMMAND_LIST[command_number]()
