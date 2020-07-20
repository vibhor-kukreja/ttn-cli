# module containing sample methods to test
from typing import AnyStr


class Command:

    def __init__(self):
        pass

    def do_hello(self, *args) -> AnyStr:
        """
        Say hello to the user
        args: List of arguments provided
        """
        return "hello {}".format(" ".join(args))
