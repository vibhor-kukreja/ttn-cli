# module containing sample methods to test
from typing import List


def do_hello(args: List) -> None:
    """
    Say hello to the user
    args: List of arguments provided
    """
    print("hello {}".format(" ".join(args)))
