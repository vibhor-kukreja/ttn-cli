from cmd import Cmd
import subprocess
from typing import Iterable


def execute(cmd) -> None:
    """
    This method executes the shell command provided and returns the output
    :param cmd:
    :return: None
    """
    popen = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             universal_newlines=True,
                             shell=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


class CommandPrompt(Cmd):
    """
    This class contains method to execute
    to see help options, enter help
    to see help on a specific command, enter help <command_name>
    Ex- help say_hi
    """
    prompt = '>'
    intro = "Welcome! Type ? to list commands"

    def do_hello(self, inp):
        """
        Say hello to the user
        Ex- hello User
        """
        print("Hey! {}".format(inp))

    def do_exit(self, inp):
        """exit the application"""
        print("Bye")
        return True

    def default(self, inp: Iterable):
        """Run in cases the above doesn't match"""
        try:
            for path in execute(inp):
                print(path, end="")
        except subprocess.CalledProcessError:
            print("Unknown command: {}".format(inp))


command_prompt = CommandPrompt()
