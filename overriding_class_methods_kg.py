"""
program: overriding_class_methods_kg.py
author: kyle godwin
last date modified: 03 april 2023

Employee class
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


class SalariedEmployee(Employee):
    """SalariedEmployee derived class from Employee base class"""
    def __init__(self, l_name, f_name, start, sal):
        super().__init__(l_name, f_name)
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


class HourlyEmployee(Employee):
    """HourlyEmployee derived class from Employee base class"""
    def __init__(self, l_name, f_name, start, pay):
        super().__init__(l_name, f_name)
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
                   f"Start date: {self._start_date}; Wage: ${self._hourly_pay:.2f}/hr")


if __name__ == "__main__":
    sal_emp = SalariedEmployee("Godwin", "Kyle", "03 April 2023", 40000)
    print(sal_emp.display())
    sal_emp.give_raise(45000)
    print(sal_emp.display())
    del sal_emp

    hr_emp = HourlyEmployee("Schwarck", "Lauren", "03 April 2023", 10.00)
    print(hr_emp.display())
    hr_emp.give_raise(12.00)
    print(hr_emp.display())
    del hr_emp

    # emp2_lname = input("Employee's last name: ")
    # emp2_fname = input("Employee's first name: ")
    # emp2_start = input("start date: ")
    # emp2_sal = int(input("Salary: "))
    # emp2 = SalariedEmployee(emp2_lname, emp2_fname, emp2_start, emp2_sal)
    # print(emp2.display())
