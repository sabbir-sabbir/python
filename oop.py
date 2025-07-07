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
# class Employee:
#     name = "Threnis"
#     language = "German"
#     salary = 120000

#     def __init__(this, name, salary, language):  
#         this.name = name
#         this.language = language
#         this.salary = salary
#         print("Im creating an object!!")
      

#     def getInfo(this):
#         print(f"The language is {this.language}. The salary is {this.salary}")
    
        

# employee_1 = Employee("Harry", 130000, "JavaScript")  
# employee_1.getInfo()  


 

# class Programmers:
#     company = "MS"
#     def __init__(self, name, salary, pincode):
#         self.name = name
#         self.salary = salary
#         self.pincode = pincode

# programmer1 = Programmers("Threnis", 120000, 9911)  
# print(programmer1.name, programmer1.salary, programmer1.pincode)     
# programmer2 = Programmers("Rohan", 130000, 7788) 
# print(programmer2.name, programmer2.salary, programmer2.pincode)



# class Calculator:
#     def __init__(self, n):
#         self.n = n 

#     def square(self):
#         print(f"The square is: {self.n*self.n}")    

# a = Calculator(4)
# a.square()
# b = Calculator(6)
# b.square()
# c = Calculator(22)
# c.square()



# test
# from random import randint

# class Train:
#     def __init__(self, trainNO):
#         self.tranNO = trainNO

#     def book(self, fro, to):
#         print(f"Ticket is booked, Train no: {self.tranNO} from {fro} to {to}")
    
#     def getStatus(self):
#         print(f"Train no: {self.tranNO} running on time, No delay")

#     def getFare(self, fro, to):
#         print(f"The ticket fare of train no: {self.tranNO} from {fro} to {to} is: 500 tk ")   


# t = Train(12399)
# t.book("Dhaka", "Rajshahi")
# t.getStatus()
# t.getFare("Dhaka", "Rajshahi")


# inheritance:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Parent:
    car = "BMW"
    money = 100000000
    home  = "Big Apartment"






class Child(Parent):
    phone = "Iphone"
    bike = "Suzuki"
