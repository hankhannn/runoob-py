class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total employees: ", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


employee1 = Employee('Hank', 1000)
employee1.displayEmployee();
employee1.displayCount()
employee2 = Employee('Eric', 2000)
employee2.displayEmployee();
employee2.displayCount()
