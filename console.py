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

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arrrrgs = arg.split()
        if arrrrgs[0] not in self.classlist.keys():
            print("** class doesn't exist **")
            return
        if len(arrrrgs) < 2:
            print("** instance id missing **")
            return
        existing_objects = storage.all()
        the_key = arrrrgs[0] + '.' + arrrrgs[1]
        if the_key in existing_objects.keys():
            the_obj = existing_objects[the_key]
            print(the_obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arrrrgs = arg.split()
        if arrrrgs[0] not in self.classlist.keys():
            print("** class doesn't exist **")
            return
        if len(arrrrgs) < 2:
            print("** instance id missing **")
            return
        existing_objects = storage.all()
        the_key = arrrrgs[0] + '.' + arrrrgs[1]
        if the_key in existing_objects.keys():
            del existing_objects[the_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.
        """
        existing_objects = storage.all()
        if len(arg) is not 0:
            for k, v in existing_objects.items():
                if arg == v.__class__.__name__:
                    print(v)
        else:
            for k, v in existing_objects.items():
                print(v)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        existing_objects = storage.all()
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classlist.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            the_key = args[0] + '.' + args[1]
            if the_key not in existing_objects.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** attribute value missing **")
            else:
                this_obj = existing_objects[the_key]
                setattr(this_obj, args[2], args[3])
                this_obj.save()        

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
