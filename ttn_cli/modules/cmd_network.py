import socket
import urllib.request
from urllib.error import URLError

from ttn_cli.utils.constants import FETCH_PUBLIC_IP_URL


def get_public_ip(*args):
    """
    function used to get public ip of your host.
    """
    try:
        ip = urllib.request.urlopen(FETCH_PUBLIC_IP_URL).read().decode("utf-8")
        print(ip)
    except URLError:
        print("Please check your internet connectivity")


def get_private_ip(*args):
    """
    function used to get private ip of your host.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
    except OSError:
        pass
    finally:
        private_ip = s.getsockname()[0]
        s.close()
    print(private_ip)
