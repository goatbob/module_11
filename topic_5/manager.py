"""
program: manager.py
author: kyle godwin
last date modified: 04 april 2023

Manager derived class utilizing Person
and Employee base classes.
"""
from topic_5.person import Person
from topic_5.employee import Employee


class Manager(Person, Employee):
    """Manger derived class from Person and Employee base classes"""
    def __init__(self, last, first, start, sal, dept, reports=[]):
        Person.__init__(self, last, first)
        Employee.__init__(self, start, sal)
        self.department = dept
        self.direct_reports = reports

    def add_report(self, a_list):
        self.direct_reports = self.direct_reports.extend(a_list)
        return self.direct_reports

    def __str__(self):
        return (f"{self.last_name}, {self.first_name}; {self.start_date}; {self.salary}; {self.department}\n"
                f"{self.direct_reports}")

    def __repr__(self):
        return (f"Manager({self.last_name}, {self.first_name}, {self.start_date}, {self.salary}, {self.department},"
                f"{self.direct_reports})")

    def display(self):
        return str(f"{self.last_name}, {self.first_name}\n"
                   f"Start date: {self.start_date}\n"
                   f"Salary: ${self.salary}\n"
                   f"Manager, department: {self.department}\n"
                   f"Direct reports: {self.direct_reports}\n")


if __name__ == "__main__":
    mgr = Manager("Godwin", "Kyle", "03 April 2023", 40000, "Data Sci")
    print(mgr.display())
    del mgr

    emp1 = Employee("05 January 1982", 35000)
    emp2 = Employee("26 June 2005", 33000)
    emp3 = Employee("07 October 2000", 33500)
    employee_list = [emp1, emp2, emp3]
    # mgr.add_report(employee_list)
    mgr = Manager("Godwin", "Kyle", "03 April 2023", 40000, "Data Sci", employee_list)
    print(mgr.display())
    del mgr

    mgr = Manager("Godwin", "Kyle", "03 April 2023", 40000, "Data Sci")
    mgr.give_raise(42000)
    print(mgr.display())
    del mgr
