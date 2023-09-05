#RISHABH SURANA (E22CSEU1029)
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if name.lower() in emp.name.lower()]
        return result

    def search_by_salary(self, condition, salary):
        if condition == '>':
            result = [emp for emp in self.employees if emp.salary > salary]
        elif condition == '<':
            result = [emp for emp in self.employees if emp.salary < salary]
        elif condition == '>=':
            result = [emp for emp in self.employees if emp.salary >= salary]
        elif condition == '<=':
            result = [emp for emp in self.employees if emp.salary <= salary]
        else:
            result = []
        return result

if __name__ == "__main__":
    db = EmployeeDatabase()
    
    db.add_employee(Employee("161E90", "Raman", 41, 56000))
    db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Select options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    option = int(input("Enter search option : "))

    if option == 1:
        age = int(input("Enter Age : "))
        result = db.search_by_age(age)
    elif option == 2:
        name = input("Enter Name : ")
        result = db.search_by_name(name)
    elif option == 3:
        condition = input("Enter salary condition (>, <, >=, <=): ")
        salary = float(input("Enter salary: "))
        result = db.search_by_salary(condition, salary)
    else:
        print("Invalid option selected.")
        result = []

    if result:
        for emp in result:
            print(emp)
    else:
        print("No Data Availabel")
