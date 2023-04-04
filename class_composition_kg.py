"""
program: class_composition_kg.py
author: kyle godwin
last date modified: 02 april 2023

Implements Person class and Student Class.
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
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


class Student:
    """Student class using Person class"""
    def __init__(self, person_info, maj, st_dat, grade):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not (name_characters.issuperset(maj)):
            raise ValueError
        if not isinstance(grade, float):
            raise ValueError
        self.person = person_info
        self.major = maj
        self.start_date = st_dat
        self.gpa = grade

    def __str__(self):
        return f"{self.person} \n{self.major}; {self.gpa}; {self.start_date}"

    def __repr__(self):
        return f"{self.person} \n{self.major}; {self.gpa}; {self.start_date}"

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def display(self):
        return f"{self.person}\nMajor: {self.major}; gpa: {self.gpa}\nStart date: {self.start_date}"


if __name__ == "__main__":
    me = Person("Godwin", "Kyle", "123 Awesome Street \n CoBo, IA 51503")
    me_stu = Student(me, "Computer Sci", "02 April 2023", 4.0)
    print(me_stu.display() + "\n")
    me_stu.change_major("Being awesome!")
    me_stu.update_gpa(3.0)
    print(me_stu.display())
    del me
    del me_stu

    me = Person("Godwin", "Kyle", "123 Awesome Street \n CoBo, IA 51503")
    me_stu = Student(me, "Computer Sci", "02 April 2023", 4)
    print(me_stu.display())
    del me
    del me_stu
