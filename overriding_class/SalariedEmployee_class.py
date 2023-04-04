"""
program: SalariedEmployee_class.py
author: kyle godwin
last date modified: 03 april 2023

SalariedEmployee derived class.
"""

from overriding_class import Employee


class SalariedEmployee(Employee):
    """SalariedEmployee derived class from Employee base class"""
    def __init__(self, l, f, start, sal):
        super().__init__(l, f)
        self._start_date = start
        self._salary = sal

    def __str__(self):
        return f"Start date: {self._start_date}; Salary: {self._salary}"

    def __repr__(self):
        return f"SalariedEmployee({self._start_date}, {self._salary})"

    def give_raise(self, new_sal):
        self._salary = new_sal

    def display(self):
        return str(f"Employee: {self.last_name}, {self.first_name}\n"
                   f"Start date: {self._start_date}; Salary: ${self._salary}")


if __name__ == "__main__":
    sal_emp = SalariedEmployee("Godwin", "Kyle", "03 April 2023", 40000)
    print(sal_emp.display())
    sal_emp.give_raise(45000)
    print(sal_emp.display())
    del sal_emp