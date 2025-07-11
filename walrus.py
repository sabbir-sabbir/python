# def sum(a: int, b: int) -> int:
#     return a + b


# print(sum(5,6))
# from typing import Tuple, List, Dict, Union

# person: Tuple[str, int] = ("Alice", 30)
# scores: Dict[str, int] = {"SABBIR": 19, "Home": 717}
# identifier: Union[str, int] = "ID123"
# Alist: List[int] = [1,2,3,4,55,6]

# print(person, scores, identifier, Alist)


try:
    a = int(input("Hey, Enter a number:  "))
    print(a)

except Exception  as e:
    print(e) 

print("Thank you")