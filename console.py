#!/usr/bin/env python3
'''Command line interpreter for HBNB Clone'''
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Class Command line interpreter
    """
    prompt = '(hbnb) '
    

    def emptyline(self):
        """
        Reprompts on an emptyline + enter
        """
        pass

    def do_exit(self, *args):
        """
        Type exit to exit the CLI program
        """
        return True

    def do_quit(self, *args):
        """
        Type quit to exit the CLI program
        """
        return True

    def do_EOF(self, arg):
        """
        Type ctrl + D to exit the programm
        """
        if not sys.stdin.isatty():
            print()

        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
