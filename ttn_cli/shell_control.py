from cmd import Cmd
from typing import AnyStr, List, Optional

from .utils.helper import get_choice, get_methods, get_help
from .modules import cmd_classes


class CommandPrompt(Cmd):
    """
    This class contains method to execute as part of shell
    For help, enter ? to show list of commands at any point
    of time.
    """
    avail_methods = None
    prompt = None
    choice = None
    intro = "Welcome! Type ? to list commands"

    def completenames(self, text, *args) -> Optional[List[str]]:
        """
        This method enables autocomplete over the available methods
        in the shell by pressing tab after writing 1 alphabet or more
        :param text: Text in the shell buffer to which complete is called
        :return: List of available methods matching the text in shell
        """
        complete_methods = \
            list(filter(lambda method_name: method_name.startswith(text),
                        list(self.avail_methods.keys()))) or \
            super().completenames(text)
        return complete_methods

    def default(self, inp: AnyStr) -> None:
        """
        This method is called every time a command is issued from shell
        :param inp: The command, i.e. a string of words issued from shell
        :return: None
        """
        command, *arguments = inp.split()
        try:
            # execute the command
            output = self.avail_methods[command](*arguments)
            print(output)
        except KeyError:
            print("Unknown command, please ? for available commands")
        except Exception as err:
            print("Following error occurred: {}".format(err))
            print("Please ? for available commands")

    def do_exit(self, inp: AnyStr = None) -> bool:
        """
        This method calls exit and closes the shell
        :param inp: String containing arguments provided after exit, if any
        :return: None
        """
        print("Goodbye Friend!")
        return True

    def do_help(self, inp: AnyStr) -> None:
        """
        This method returns and displays a list of commands available
        For user to run based on choice selected
        :param inp: String of arguments provided after help or ?, if any
        :return: None
        """
        options = list(self.avail_methods.keys())
        options.append("exit")
        print(get_help(options))

    def emptyline(self) -> None:
        """
        This method overrides the flow when enter key is pressed and
        no command is provided, and hence does nothing.
        :return: None
        """
        pass

    def preloop(self) -> None:
        """
        This method is executed for the first and only time when
        the shell is activated from the terminal, with purpose
        to receive the choice from user
        :return: None
        """
        self.choice = get_choice(cmd_classes)
        # until a valid choice is selected, repeat this
        if self.choice is None:
            self.preloop()

        choice_module = cmd_classes[self.choice]

        # get methods present in the module selected as choice above
        self.avail_methods = get_methods(choice_module)
        self.prompt = '({})>'.format(cmd_classes[self.choice])


command_prompt = CommandPrompt()
