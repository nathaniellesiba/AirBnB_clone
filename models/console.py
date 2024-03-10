#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the command interpreter when EOF is reached"""
        return True

    def do_quit(self, line):
        """Exit the command interpreter"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.cmdloop()
