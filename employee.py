class Employee:

    def __init__(self, name: int, age: int, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name}-{self.age}-{self.salary}"
