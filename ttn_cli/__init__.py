from .shell_control import command_prompt


def main() -> None:
	"""
	This method returns a shell control to the user to execute commands
	:return:
	"""
	command_prompt.cmdloop()


if __name__ == "__main__":
	main()
