from overriding_class import Person
from overriding_class import SalariedEmployee


class Manager(Person, SalariedEmployee):
    """Manger derived class from Person and Employee base classes"""
    def __init__(self, last, first, start, dept, sal, rept={}):
        super().__init__(last, first, start, sal)
        self._department = dept
        self._direct_reports = rept

    def display(self):
        return str(f"{self.last_name}, {self.first_name}"
                   f"Start date: {self._start_date}"
                   f"Salary: ${self._salary}"
                   f"Department: {self._department}")


if __name__ == "__main__":
    mgr = Manager("Godwin", "Kyle", "03 April 2023", "Data Sci", 40000)
    print(mgr.display())
