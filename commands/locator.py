from .open_chrome import OpenChrome
from .open_slack import OpenSlack
from .open_spotify import OpenSpotify


class Locator:
    COMMAND_LIST = {
        "1": OpenChrome,
        "2": OpenSpotify,
        "3": OpenSlack
    }

    def find(self, command_number: str):
        command_class = self.COMMAND_LIST[command_number]

        if command_class is None:
            raise Exception("Class command not found")

        return command_class()
