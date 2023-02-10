#!/usr/bin/env python3
'''Filestorage class to serialize instances to a JSON fil
e  and deserialize JSON file to instances
'''
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """

        FileStorage.__objects[f"{obj.__class__.name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the json file (path:__file_path)
        """

        ourdict = {}
        if not self.__objects:
            for key, value in self.__objects.items():
                ourdict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(ourdict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists;
        """
        try:
            with open(self.__file_path, "r") as stored_data:
                loaded_data = json.load(stored_data)
        except FileNotFoundError:
            pass
