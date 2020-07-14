# File containing helper methods to facilitate shell_control
import subprocess
from importlib import import_module
import inspect
from typing import List, AnyStr, Union, Dict


def get_menu(list_of_modules: List) -> AnyStr:
    """
    This method will return a menu of available modules from the list
    :param list_of_modules: List containing choices to display as menu options
    :return: String formatted menu
    """
    display_menu = "\n".join(
        ["{}.{}".format(index, item)
         for index, item
         in enumerate(list_of_modules)])
    return display_menu


def get_choice(list_of_modules: List) -> Union[int, None]:
    """
    This method will display a menu of available modules to choose from
    and then return the user choice based on input
    :param list_of_modules:
    :return:
    """
    display_menu = get_menu(list_of_modules)
    try:
        choice = int(input("{}\nEnter A Choice(Number):".format(display_menu)))
        if not choice < len(list_of_modules):
            raise ValueError
        return choice
    except ValueError:
        print("Invalid choice, please try again")
        return None


def get_methods(class_name: AnyStr) -> Dict:
    """
    This method will load methods from given module name
    :param class_name: String name of the choice selected to extract methods
    :return: A Dictionary containing mapping between function name and ref.
    """
    methods = dict()
    try:
        module = import_module("ttn_cli.modules.cmd_{}".format(class_name))

        class_tuple = \
            dict(inspect.getmembers(module, predicate=inspect.isclass))

        # will call init method
        class_object = class_tuple['Command']()

        # below gets the public methods out of the chosen module
        # and rejects other private and protected methods
        avail_methods = \
            [method for method in
             inspect.getmembers(class_object,
                                predicate=inspect.ismethod)
             if not method[0].startswith("_")]

        # create a dict for menu of available methods
        for name, method in avail_methods:
            methods.update({name: method})
        return methods
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Invalid choice for module")


def get_help(avail_methods: List) -> None:
    """
    Method to display menu of available methods in the chosen shell
    :param avail_methods: List containing
    :return:
    """
    print("Feel free to run any of these")
    help_menu = get_menu(avail_methods)
    return help_menu


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
