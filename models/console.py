#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """is a simple CRUD command
    for EOF, quiting, prompt, help"""

    prompt = "(hbnb)"

    def do_EOF(seld, line):
        """this execute end of file"""
        print()
        return True

    def do_default(self, line):
        print(f"unknown command; {line}")

    def help welcoming(self):
        """this is a customized or
        detailed help"""
        print('/n'.join([
            'welcoming [person]']))

    def emptyline(self):
        """this is printing empty
        line notification"""
        print("you have entered empty line")

    def do_quit(self, line):
        return True 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
