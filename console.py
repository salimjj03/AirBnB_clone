#!/usr/bin/python3
""" This module contains the entry point
of the command interpreter.

"""

import sys
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id.
        """

        if args and args == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)
        elif args:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """ Prints the string representation of an
        instance based on the class name and id.
        """

        if args:
            if args[:9] == "BaseModel":
                try:
                    class_n, c_id = args.split(" ")
                except Exception:
                    print("** instance id missing **")
                else:
                    if class_n == "BaseModel":
                        dic = storage.all()
                        key = ".".join([class_n, c_id])
                        if key in dic:
                            print(dic[key])
                        else:
                            print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """ This Method  Deletes an instance based on
        the class name and id (save the change into the JSON file).
        """

        if args:
            if args[:9] == "BaseModel":
                try:
                    class_n, c_id = args.split(" ")
                except Exception:
                    print("** instance id missing **")
                else:
                    if class_n == "BaseModel":
                        dic = storage.all()
                        key = ".".join([class_n, c_id])
                        if key in dic:
                            del dic[key]
                            storage.save()
                        else:
                            print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """ This Method  Prints all string representation of
        all instances based or not on the class name.
        """

        if args == "BaseModel":
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
            if args[0] != "BaseModel":
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
                    obj.name = args[3][1:-1]
                else:
                    obj.name = int(args[3])
                storage.save()
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
