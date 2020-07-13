# module containing network related methods
import socket
import urllib.request
from typing import List
from urllib.error import URLError

from ttn_cli.utils.constants import FETCH_PUBLIC_IP_URL


def get_public_ip(args: List) -> None:
    """
    Function used to get public ip of your host.
    args: List of arguments provided
    """
    try:
        ip = urllib.request.urlopen(FETCH_PUBLIC_IP_URL).read().decode("utf-8")
        print(ip)
    except URLError:
        print("Please check your internet connectivity")


def get_private_ip(args: List) -> None:
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
    print(private_ip)
