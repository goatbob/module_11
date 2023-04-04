from overriding_class import Person
from overriding_class import Employee


class Manager(Person, Employee):
    """Manger derived class from Person and Employee base classes"""
    def __init__(self, last, first, start, sal, dept, rept=[]):
        super().__init__(last, first, start, sal)
        self._department = dept
        self._direct_reports = rept

    def display(self):
        return str(f"{self.last_name}, {self.first_name}"
                   f"Start date: {self.start_date}"
                   f"Salary: ${self.salary}"
                   f"Department: {self._department}")


if __name__ == "__main__":
    mgr = Manager("Godwin", "Kyle", "03 April 2023", 40000, "Data Sci")
    print(mgr.display())
