"""
file = open("student.txt", "r+")
# print(file.writable())
text = file.read()
print(text)
size = len(text)
print(size)
file.close()

file = open("student.txt", "r+")
text = file.readlines()[0]
print(text)

file = open("student.txt", "r+")
for line in file:
    print(line)
"""