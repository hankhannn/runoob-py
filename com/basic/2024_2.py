class Employee:
    # 雇员信息
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total employees: ", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def prt(self):
        print(self)
        print(self.__class__)


employee1 = Employee('Hank', 1000)
employee1.displayEmployee()
employee1.displayCount()

employee2 = Employee('Eric', 2000)
employee2.displayEmployee()
employee2.displayCount()

employee2.prt()

print("Total Employee", Employee.empCount)

print("hasattr name", hasattr(employee2, "name"))
print("hasattr age", hasattr(employee2, "age"))
print("setattr age", setattr(employee2, "age", 32))
print("hasattr age", hasattr(employee2, "age"))
print("delattr age", delattr(employee2, "age"))
print("hasattr age", hasattr(employee2, "age"))
employee2.address = "Shanghai"
print(employee2.__dict__)
print(employee2.__doc__)
print(employee2.__module__)
