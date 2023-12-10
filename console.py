#!/usr/bin/python3
""" This module contains the entry point
of the command interpreter.

"""

import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


airbnb_class = ["BaseModel", "User"]


class HBNBCommand(cmd.Cmd):
    """ This module contains the entry point
    of the command interpreter.

    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ This model quite the interpreter """

        return True

    def do_EOF(self, args):
        """ This method quite the interpreter using ctr+D. """

        return True

    def emptyline(self):
        """ This model quite the interpreter """

        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id.
        """

        args = arg.split()
        if args:
            if args[0] not in airbnb_class:
                print("** class doesn't exist **")
            else:
                class_ = globals()[args[0]]
                obj = class_()
                obj.save()
            print(obj.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """ Prints the string representation of an
        instance based on the class name and id.
        """

        args = arg.split()
        if args:
            if args[0] not in airbnb_class:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                dic = storage.all()
                key = ".".join([args[0], args[1]])
                if key in dic:
                    print(dic[key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ This Method  Deletes an instance based on
        the class name and id (save the change into the JSON file).
        """

        args = arg.split()
        if args:
            if args[0] not in airbnb_class:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                dic = storage.all()
                key = ".".join([args[0], args[1]])
                if key in dic:
                    del dic[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """ This Method  Prints all string representation of
        all instances based or not on the class name.
        """

        args = arg.split()
        if args[0] in airbnb_class:
            ls = []
            dic = storage.all()
            for key in dic:
                ls.append(dic[key].__str__())
            print(ls)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ This Method Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        """

        args = arg.split()
        if args:
            if args[0] not in airbnb_class:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                dic = storage.all()
                key = "{}.{}".format(args[0], args[1])
                obj = dic[key]
                name = args[2]
                if args[3][0] == '"':
                    setattr(obj, args[2], args[3][1:-1])
                else:
                    setattr(obj, args[2], int(args[3]))
                storage.save()
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
