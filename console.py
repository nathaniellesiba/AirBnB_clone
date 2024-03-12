#!/usr/bin/python3

import cmd
import sys
import json
import os
from models import BaseModel


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


"""---------CRUD--------------"""


def do_create(self, line):
    """Creates a new instance of
    BaseModel, saves it (to the
    JSON file) and prints the id
    """
    args = line.split()
    if len(args) == 2:
        digit, name = args
        self.user[digit] = name
        print(f"** class name missing **")
        else:
            print("input is not valid")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
