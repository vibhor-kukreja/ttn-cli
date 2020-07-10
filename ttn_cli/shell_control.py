from cmd import Cmd

from .utils.helper import get_choice, get_methods, get_help
from .modules import cmd_classes


class CommandPrompt(Cmd):
    """
    This class contains method to execute
    to see help options, enter help
    to see help on a specific command, enter help <command_name>
    Ex- help say_hi
    """
    avail_methods = None
    prompt = None
    choice = None
    intro = "Welcome! Type ? to list commands"

    def default(self, inp):
        """Run in cases the above doesn't match"""
        command, *arguments = inp.split()
        try:
            self.avail_methods[command](arguments)
        except KeyError:
            print("Unknown command, please ? for available commands")

    def do_exit(self, inp):
        print("Goodbye Friend!")
        return True

    def do_help(self, inp: str):
        options = list(self.avail_methods.keys())
        options.append("exit")
        print(get_help(options))

    def emptyline(self):
        pass

    def preloop(self):
        self.choice = get_choice(cmd_classes)
        if self.choice is None:
            self.preloop()

        choice_module = cmd_classes[self.choice]
        self.avail_methods = get_methods(choice_module)
        self.prompt = '({})>'.format(cmd_classes[self.choice])

    # def do_leave(self, inp):
    #     self.preloop()


command_prompt = CommandPrompt()
