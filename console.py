#!/usr/bin/python3
"""This module hosts the HBNBCommand class which inherits from the Cmd class.
"""
import cmd
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Entry point Class HBNBCommand
    defines a prompt (hbnb)

    public class methods:
        do_quit - handles quit command
        do_EOF - handles exit using EOF
    """

    prompt = "(hbnb) "
    __models = ["BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, arg: str) -> bool | None:
        """Help command to show the help of the console"""
        return super().do_help(arg)

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # prints a new line
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id.

        example usage:
        (hbnb) show BaseModel 1234-5665-4321
        """

        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            print(retrieved_record)
        except Exception:
            pass

    def do_destroy(self, arg):
        """Destroys an instance of a class based on the class name and id.

        Example usage:
        (hbnb) destroy BaseModel 1234-5665-4321
        """

        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            storage.destroy(retrieved_record)
        except Exception:
            pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.

        example usage:
        (hbnb) all
        (hbnb) all BaseModel
        """

        if not arg:
            # Print all instances
            instances = storage.all()
            instance_list = []
            for instance in instances.values():
                instance_list.append(str(instance))
            print(instance_list)
        else:
            class_name = arg.strip()
            if class_name not in self.__models:
                print("** class doesn't exist **")
                return
            # Print instances of a specific class
            file_storage = storage._FileStorage__objects
            instance_list = []
            for instance in file_storage.values():
                if instance["__class__"] == class_name:
                    instance_list.append(str(instance))
            print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)

        example usage:
        (hbnb) update BaseModel 1234-5676-4321 email "aibnb@mail.com" """

        args = self.get_update_args(arg)

        if args is None:
            return

        [class_name, instance_id, attribute, value] = args

        try:
            record = self.find_record(class_name, instance_id)

            # if record is None:
            #     print('** no instance found **')
            #     return

            retrieved_record = globals()[class_name](**record)
            setattr(retrieved_record, attribute, value)
            setattr(retrieved_record, "updated_at", datetime.now())
            storage.new(retrieved_record)
        except Exception:
            pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
