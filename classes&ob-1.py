class Employee:
    company = "Google"
    role = "SDE"
    salary = "50000"

    @staticmethod
    def get_salary():
        print(f"salary is {Employee.salary}")
    
    def get_info(self):
        print(f"company of this employee is {self.company} with the role of {self.role}")

e1 = Employee()
# print(e1.role)
e1.get_info()
e1.get_salary()

e2 = Employee()
e2.company = "OpenAI"
e2.role = "AI Developer"
e2.salary = 65000
e2.get_info()