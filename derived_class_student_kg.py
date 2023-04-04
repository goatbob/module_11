"""
program: derived_class_student_kg.py
author: kyle godwin
last date modified: 02 april 2023

Implements Student derived class from
Person base class.
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=""):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def __str__(self):
        return f"{self.last_name}, {self.first_name} \n {self.address}"

    def __repr__(self):
        return f"{self.last_name}, {self.first_name} \n {self.address}"

    def display(self):
        return f"{self.last_name}, {self.first_name}"


class Student(Person):
    """Student derived class from Person base class"""
    def __init__(self, stu_id, l_name, f_name, maj="Computer Science", grade=0.0):
        super().__init__(l_name, f_name)
        self.student_id = stu_id
        self.major = maj
        self.gpa = grade

    def display(self):
        return f"{self.last_name}, {self.first_name}:({self.student_id}) {self.major} gpa: {self.gpa}"


if __name__ == "__main__":
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student
