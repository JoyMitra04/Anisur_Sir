"""
try:
   list = [20, 0, 30]
   result = list[0] / list[1]
   print(result)
   print("done")
except ZeroDivisionError:
    print("division by zero")
print("Succesful")

try:
   list = [20, 0, 30]
   result = list[0] / list[3]
   print(result)
   print("done")
except ZeroDivisionError:
    print("division by zero is not possible")
except IndexError:
    print("list index out of range")
print("Succesfull")

try:
   num = int(input())
   div = 20 / num
   print(div)
   print("done")
except ValueError:
    print("unsupported operand type")
finally:
    print("Succesfully")
"""