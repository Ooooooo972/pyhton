class Person:
    def __init__(self):
        self.__name = "Geeks"  # private attribute
        self.__age = 10        # private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
