# class in python::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# instance vs class atributes
# class Employee:
#     name = "Threnis"
#     language = "German"
#     salary = 120000

# EmployeeNumber_1 = Employee()
# EmployeeNumber_1.name = "Threnis"
# print(EmployeeNumber_1.name, EmployeeNumber_1.salary, EmployeeNumber_1.language)


# self  parameter (We can modify it by any name)::::::::::::::::::::::::::::::::::::::::::::::::::::::
# class Employee:
#     name = "Threnis"
#     language = "German"
#     salary = 120000

#     def getInfo(this):
#         print(f"The language is {this.language}. The salary is {this.salary}")

#     def greet(this):
#         print(f"Good morning {this.name}")     

# employee_1 = Employee()  
# employee_1.getInfo()      
# employee_1.greet()   





# constructor::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Employee:
    name = "Threnis"
    language = "German"
    salary = 120000

    def __init__(this, name, salary, language):  
        this.name = name
        this.language = language
        this.salary = salary
        print("Im creating an object!!")
      

    def getInfo(this):
        print(f"The language is {this.language}. The salary is {this.salary}")
    
        

employee_1 = Employee("Harry", 130000, "JavaScript")  
employee_1.getInfo()  


 







