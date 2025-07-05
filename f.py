# def avg():
#     a = 12
#     b = 13
#     c = 14

#     average = (a+b+c)/3
#     print(average)

# avg()
# print("Thank you")
# avg()
# print("Thank you")
# avg()



# def goodDay():
#     name = input("Enter your name get greet:  ")
#     print("Good Morning", name)

# goodDay()    


# def goodDay(name, ending="Thanks ++"):
#     print("Good day", name)
#     print(ending,name)


# goodDay("SABBIR", "THANK YOU SO MUCH")



# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter the number:  "))
# print(f"The factorial of this number is: {factorial(n)}")


# def inc_to_cms(inch):
#     return inch * 2.54

# print(round(inc_to_cms(45)))


list = ["Harry", "Rohan", "Shovam", "an"]

def removeN(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n        
    
print(removeN(list, "an"))
