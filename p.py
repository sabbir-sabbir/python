import os
from typing import List
from functools import reduce



# reduc.......................................................
# MyList: List[int] = [1,2,3,4,5,6,7,8]

# def sum(a, b):
#     return a + b

# print(reduce(sum, MyList))
# reduc.......................................................

# Filter.....................................................
# MyList: List[int] = [1,2,3,4,5,6,7,8]

# def even(n):
#     if(n%2 == 0):
#         return True
#     else:
#         return False
    
# onlyEven = filter(even, MyList)  
# print(list(onlyEven))
# Filter.....................................................  


# MAP...................................................
# MyList: List[int] = [1,2,3,4,5,6,7]

# square = lambda x: x*x

# NewSquareList = map(square, MyList)
# print(list(NewSquareList))
# MAP...................................................


# A: List[str] = ["code", "With", "Harry"] 
# final  = "(*__*)".join(A)
# print(final)



# Mylist: List[int] = [1,2,3,4,5,6,7,8,9]

# for i, item in enumerate(Mylist):
#     if i == 2 or i == 4 or i == 6:
#         print(item)




        # def FileCreationFunc():
#     if os.path.exists("1.txt"):
#         with open("1.txt", "r") as f:
#             print(f.read())
#     else:
#         with open("1.txt", "w") as f:
#             f.write("This file was just created because it didn't exist.\n")
#         print("1.txt was not found, so it has been created with default content.")


# FileCreationFunc()