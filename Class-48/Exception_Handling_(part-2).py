"""
try:
   num1 = int(input())
   num2 = int(input())
   result = num1 / num2
   print(result)
   print("done")
except ZeroDivisionError:
    print("you can not divide by a number 0")
except ValueError:
    print("you have to insert int number")
finally:
    print("Thanks")
"""

age = int(input())
def voter (age):
    if age < 18:
        raise ValueError("invaild Voter")
    return "you are allow to vote"
try:
   print(voter(age))
except ValueError:
    print("invaild voter")
finally:
    print("Thanks !!!")