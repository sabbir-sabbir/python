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
# class Parent:
#     car = "BMW"
#     money = 100000000
#     home  = "Big Apartment"






# class Child(Parent):
#     phone = "Iphone"
#     bike = "Suzuki"



# k = Child()
# print(k.car)



# class Programmer:
#     def __init__(self):
#         print("This is Programmer class")


# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()  # Calls Programmer.__init__()
#         print("This is Manager class")

#     def __str__(self):
#         return "This is a New object"


# newObject = Manager()
# print(newObject)




# class Programmer:
#     def __init__(self):
#         print("This is Programmer class")


# class Programmer2:
#     def __init__(self):
#         print("This is Programmer2 class")


# class Manager(Programmer, Programmer2):
#     def __init__(self):
#         Programmer.__init__(self)     # manual call to Programmer's constructor
#         Programmer2.__init__(self)    # manual call to Programmer2's constructor
#         print("This is Manager class")


# newObject = Manager()
# print(newObject)









# class Number:
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, num) :
#         return self.n + num.n   
        


# n = Number(12)
# m = Number(13)

# print(n + m)











# class TwoDVector:
#     def __init__(self, i, j):
#         self.i = i 
#         self.j = j
#     def show(self):
#         print(f"The vector is: {self.i}i + {self.j}j ")

# class ThreeDVector(TwoDVector):
#     def __init__(self, i, j, k):
#          super().__init__(i, j)
#          self.k = k

#     def show(self):
#         print(f"The vector is: {self.i}i + {self.j}j + {self.k}k ")

# a = TwoDVector(1, 2)
# a.show()
# b = ThreeDVector(1,2,3)
# b.show()




# class Student:
#     name = "SABBIR"


# s1 = Student()
# s2 = Student()
# print(s1.name)    
# print(s2.name)


class Car:
    color = "Blue"
    Brand = "BMW"


car1 = Car()
print(car1.color)    
print(car1.Brand)    