# module containing network related methods
import socket
import urllib.request
from typing import List, AnyStr
from urllib.error import URLError

from ttn_cli.utils.constants import FETCH_PUBLIC_IP_URL


class Command:

    def __init__(self):
        pass

    def get_public_ip(self, *args) -> AnyStr:
        """
        Function used to get public ip of your host.
        args: List of arguments provided
        """
        try:
            ip = urllib.request.urlopen(FETCH_PUBLIC_IP_URL).read().decode(
                "utf-8")
            return ip
        except URLError:
            return "Please check your internet connectivity"

    def get_private_ip(self, *args) -> None:
        """
        Function used to get private ip of your host.
        args: List of arguments provided
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
        except OSError:
            # will be raised when the user isn't connected to any network
            # no resolution required as latter code will work in any case
            pass
        finally:
            private_ip = s.getsockname()[0]
            s.close()
        return private_ip


cmd_network = Command()
