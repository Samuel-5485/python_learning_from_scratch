# for loop
for i in range(1, 9, 3): 
    print(i)

for i in range(1, 10):
    print("Learn Machine Learning")

for i in range(5):
    print(i)

for i in range(10, 1, -2):
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
for i in range(len(fruits)):
    print(fruits[i])

for i in range(-3,5):
    print(i)

for i in range(1,4):
    square = i*i
    print(square)

x = [1, 3,4,-1,2,5]
for data in x:
    if data<0:
        break
    print(data)

for data in x:
    if data<0:
        continue
    print(data)

# Use a while loop, for loop and break statement to write a program that accepts
# names of student repteatedly until a user enters a word "close"
student_name = []
while True:
    name = input("Enter student name: ")
    if name == "close":
        break
    student_name.append(name)
print("The names of the students are: ")
for name in student_name:
    print(name)

# write a program that prints all the even numbers from 1 to 50

for i in range(0, 50, 2):
    print(i)

# write a program that calculates and display factorial of a given numbers
fact = 1
num = int(input("Enter a number: "))
for i in range(num, 1, -1):
    fact = fact*i
print("The factoral of", num, "is", fact)

# write a program that accepts a number until a negative number is entered .
# once the negatice number is entered show the maximum of those numbers
num = []
while True:
    n = float(input("Enter the number: "))
    if n < 0:
        break
    num.append(n)
print("List of numbers that your entered.")
for numbers in num:
    print(numbers)

# write a program that show table of multiplication from 1 to 4 in python
for i in range(1, 5):
    print("Multiplication table of", i)
    for j in range(1, 5):
        print(i, "*", j, "=", i*j)
    print("-----------")

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

for i in range(1, 4):
    for j in range(1, i):
        print("*", end=" ")
    print()