class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is 100k")
        print(f"Salary is {self.salary} in {self.company}")


afsar = Employee()
arshi = Employee()
afsar.salary=10000000
afsar.getSalary()
Employee.getSalary(afsar)
afsar.getSalary="500k"
print(afsar.getSalary)
