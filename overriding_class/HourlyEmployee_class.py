"""
program: HourlyEmployee_class.py
author: kyle godwin
last date modified: 03 april 2023

HourlyEmployee derived class.
"""

from overriding_class.Employee_class import Employee


class HourlyEmployee(Employee):
    """HourlyEmployee derived class from Employee base class"""
    def __init__(self, l, f, start, pay):
        super().__init__(l, f)
        self._start_date = start
        self._hourly_pay = pay

    def __str__(self):
        return f"Start date: {self._start_date}; Salary: {self._hourly_pay}"

    def __repr__(self):
        return f"SalariedEmployee({self._start_date}, {self._hourly_pay})"

    def give_raise(self, new_pay):
        self._hourly_pay = new_pay

    def display(self):
        return str(f"Employee: {self.last_name}, {self.first_name}\n"
                   f"Start date: {self._start_date}; Wage: ${self._hourly_pay:.2f}/hr\n")


if __name__ == "__main__":
    hr_emp = HourlyEmployee("Schwarck", "Lauren", "03 April 2023", 10.00)
    print(hr_emp.display())
    hr_emp.give_raise(12.00)
    print(hr_emp.display())
    del hr_emp
