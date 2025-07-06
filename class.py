# class in python
# instance vs class atributes
# class Employee:
#     name = "Threnis"
#     language = "German"
#     salary = 120000

# EmployeeNumber_1 = Employee()
# EmployeeNumber_1.name = "Threnis"
# print(EmployeeNumber_1.name, EmployeeNumber_1.salary, EmployeeNumber_1.language)


# self  parameter (We can modify it by any name)::
class Employee:
    name = "Threnis"
    language = "German"
    salary = 120000

    def getInfo(this):
        print(f"The language is {this.language}. The salary is {this.salary}")

employee_1 = Employee()  
Employee.getInfo(employee_1)      



