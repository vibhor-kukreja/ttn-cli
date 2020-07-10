import subprocess
from importlib import import_module
import inspect


def get_menu(list_of_modules):
    """
    This method will return a menu of available modules from the list
    :param list_of_modules:
    :return:
    """
    # list_of_modules.append("exit")
    display_menu = "\n".join(
        ["{}.{}".format(index, item)
         for index, item
         in enumerate(list_of_modules)])
    return display_menu


def get_choice(list_of_modules: list):
    """
    This method will display a menu of available modules to choose from
    and then return the user choice based on input
    :param list_of_modules:
    :return:
    """
    display_menu = get_menu(list_of_modules)
    try:
        choice = int(input("{}\nEnter A Choice:".format(display_menu)))
        if not choice < len(list_of_modules):
            raise ValueError
        return choice
    except ValueError:
        print("Invalid choice, please try again")
        return None


def get_methods(class_name):
    """
    This method will load methods from given module name
    :param class_name:
    :return:
    """
    methods = dict()
    try:
        module = import_module("ttn_cli.modules.cmd_{}".format(class_name))
        methods_tuple = \
            inspect.getmembers(module, predicate=inspect.isfunction)
        for name, method in methods_tuple:
            methods.update({name: method})
        return methods
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Invalid choice for module")


def get_help(avail_methods):
    """
    Method to display menu of available methods in the chosen shell
    :param avail_methods:
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
