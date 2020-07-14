import sys

from .cli import cli
from .shell_control import command_prompt


def main() -> None:
    """
    This is the main function which returns a shell to user as well
    as can run cli commands directly.
    """
    if len(sys.argv) > 1:
        cli()
    else:
        command_prompt.cmdloop()


if __name__ == "__main__":
    main()
