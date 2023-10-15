#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, arg: str) -> bool | None:
        """Help command to show the help of the console"""
        return super().do_help(arg)

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass
    
    def do_create(self, arg):
        """Create command to create a new instance"""
        if not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        """Show command to show an instance"""
        if not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
        


if __name__ == "__main__":
    HBNBCommand().cmdloop()
