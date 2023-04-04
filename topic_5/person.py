
class Person:
    """Person class"""
    def __init__(self, lname, fname, addy="", phone=""):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phone

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def __repr__(self):
        return f"{self.last_name}, {self.first_name}"

    def display(self):
        return f"{self.last_name}, {self.first_name}"
