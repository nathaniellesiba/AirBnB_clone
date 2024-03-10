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


# Assuming BaseModel is the base model class


def create_class(args):
    """Creates a new instance of
    BaseModel, saves it (to the
    JSON file) and prints the id
    """
    if len(args) < 2:
        print("** class name missing **")
        return

    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return

    new_instance = globals()[class_name]()
    new_instance.save()
    print(new_instance.id)


def show_instance(args):
    """Prints the string representation
    of an instance based on the 
    class name and id
    """
    if len(args) < 3:
        print("** class name missing **" if len(args) < 2 else "** instance id missing **")
        return

    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return

    instance_id = args[2]
    all_instances = BaseModel.load_instances()
    for instance in all_instances.get(class_name, []):
        if instance.id == instance_id:
            print(instance)
            return

    print("** no instance found **")


def destroy_instance(args):
    """Deletes an instance based
    on the class name and id 
    (save the change into JSON file)
    """
    if len(args) < 3:
        print("** class name missing **" if len(args) < 2 else "** instance id missing **")
        return

    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return

    instance_id = args[2]
    all_instances = BaseModel.load_instances()
    for instance_list in all_instances.values():
        for instance in instance_list:
            if instance.id == instance_id:
                instance_list.remove(instance)
                BaseModel.save_instances(all_instances)
                return

    print("** no instance found **")


def show_all_instances(args):
    """Prints all string representation
    of all instances based or 
    not on the class name. 
    """
    if len(args) < 2:
        all_instances = BaseModel.load_instances()
        for instance_list in all_instances.values():
            for instance in instance_list:
                print(instance)
    else:
        class_name = args[1]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        all_instances = BaseModel.load_instances()
        for instance in all_instances.get(class_name, []):
            print(instance)


def update_instance(args):
    """Updates an instance based on 
    the class name and id by adding or
    updating attribute (save the
    change into the JSON file)
    """
    if len(args) < 4:
        print("** class name missing **" if len(args) < 2 else
              ("** instance id missing **" if len(args) < 3 else "** attribute name missing **"))
        return

    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return

    instance_id = args[2]
    attribute_name = args[3]
    if attribute_name not in BaseModel.__dict__:
        print("** attribute name missing **")
        return

    attribute_value = " ".join(args[4:])
    if not attribute_value or (len(attribute_value) > 1 and attribute_value[0] != '"' and attribute_value[-1] != '"'):
        print("** value missing **")
        return

    attribute_value = attribute_value[1:-1] if len(attribute_value) > 1 else attribute_value
    all_instances = BaseModel.load_instances()
    for instance_list in all_instances.values():
        for instance in instance_list:
            if instance.id == instance_id:
                setattr(instance, attribute_name, type(getattr(BaseModel, attribute_name))(attribute_value))
                instance.save()
                return

    print("** no instance found **")


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else ""

    if command == "create":
        create_class(sys.argv)
    elif command == "show":
        show_instance(sys.argv)
    elif command == "destroy":
        destroy_instance(sys.argv)
    elif command == "all":
        show_all_instances(sys.argv)
    elif command == "update":
        update_instance(sys.argv)
    else:
        print("** command not found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    main()
