#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """This class implements a simple CRUD command interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the command interpreter when EOF is reached."""
        return True

    def do_default(self, line):
        """Handle unknown commands."""
        print(f"Unknown command: {line}")

    def help_welcoming(self):
        """Display help for the 'welcoming' command."""
        print("Usage: welcoming [person]")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, line):
        """Exit the command interpreter."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
