#!/usr/bin/python3
""" This module contains the entry point
of the command interpreter.

"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

