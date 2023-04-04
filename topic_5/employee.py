
class Employee():
    """Employee class"""
    def __init__(self, start, sal):
        self.start_date = start
        self.salary = sal

    def __str__(self):
        return f"Start date: {self.start_date}; Salary: {self.salary}"

    def __repr__(self):
        return f"Employee({self.start_date}, {self.salary})"

    def give_raise(self, new_sal):
        self.salary = new_sal

    def display(self):
        return str(f"Start date: {self.start_date}; Salary: ${self.salary}")