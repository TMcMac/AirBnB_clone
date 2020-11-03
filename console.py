#!/usr/bin/env python3
'''Command line interpreter for HBNB Clone'''
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Class Command line interpreter
    """
    prompt = '(hbnb) '
    classlist = {'BaseModel': BaseModel}

    def do_create(self, arg):
        """
        Type create and a class name to create an instance of that class
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        new_obj = None
        for key, value in self.classlist.items():
            if key == arg:
                new_obj = value()
        if new_obj is None:
            print("** class doesn't exist **")
            return
        storage.new(new_obj)
        storage.save()
        print(new_obj.id)

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
