"""
program: Employee_class.py
author: kyle godwin
last date modified: 03 april 2023

Employee base class.
"""


class Employee:
    """Employee Class"""
    def __init__(self, lname, fname, addr="", ph_num=""):  # initialize employee variables
        self.last_name = lname
        self.first_name = fname
        self.address = addr
        self.phone_number = ph_num

    def __str__(self):  # string out put for class
        return f"{self.first_name}, {self.last_name}, {self.address}, {self.phone_number}"

    def __repr__(self):  # representation output for class
        return f"Employee({self.last_name}, {self.first_name}, {self.address}, {self.phone_number}"

    def display(self):  # formatted display of class
        return str(f"{self.first_name} {self.last_name} \n"
                   f"{self.address}\n{self.phone_number}")


