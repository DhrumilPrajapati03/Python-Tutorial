class Employee:
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    @staticmethod
    def get_salary():
        print(f"salary is {Employee.salary}")
    
    def get_info(self):
        print(f"Name of this employee is {self.name} with the role of {self.role}")


e1 = Employee("john", 50000, "SDE")
e1.get_info()

e2 = Employee("karan",65000,"AI DEV")
e2.get_info()