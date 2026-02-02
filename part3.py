# in this you gonna leaern bool, if else, nested if, if elif else
# Comparison Operators: ==, !=, >,<,>=,<=
a = 10
b = 20
c = not a == b
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(c)

# Boolean Oerators: and, or, not
x = 5
y = 10
print(x<10 and y>5)
print(x>7 and y>5)
print(x<7 or y>5)

user_name = "admin"
password = "1234"
if user_name == "admin" and password == "1224":
    print("Access granted")
else:
    print("Access denied")

# Control flows
"""
programs have 4 basic Control Flows:
1.Sequencial flow
2.Desision making(if, if else, nested if, if elif else) 
3.Loops(for, while)
4.Jump Statements(break, continue, pass, return)
"""
# If statements
age = 18
if age >= 18:
    print("You are eligible to vote")

# use of it statements
num = float(input("Enter the number:"))
if num >=0:
    print("The number is positive")
else:
    print("The number is negative")

# write a program to check whether the number is even or odd
num = int(input("Enter the number:"))
if num%2 ==0:
    print("The number is even")
else:
    print("The number is odd")

# Write a program to determine if a student is eligible to vote based on their age.
age = int(input("Enter your age:"))
if age>=18:
    print("You're eligible to vote")
else:
    print("You're not eligible to vote yet")

# Nested if statements
a = 89
b = 67
c = 90

if a>b:
    if a>c:
        print("a is the largest number")
    else:
        print("c is the largest number")
elif b>c:
    print("b is the largest number")
else:
    print("c is the largest number")

# Write a program that accept student score and display the grade
score = float(input("Hye, what is your score?"))
if score >=90:
    print("Your grade is A+")
elif score >=80:
    print("Your grade is A")
elif score >=70:
    print("Your grade is B")
elif score >=60:
    print("Your grade is C")
elif score >=50:
    print("Your grade is D")
else:
    print("Your grade is F, \n you need to take the course again")

# if-elif-else
# Write a python program to determine the largest of the three numbers

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000

total_item = int(input("Enter how many items did you purchase: "))
initial_cost = total_item*100
if initial_cost > 1000:
    initial_cost = initial_cost - (initial_cost * 0.1)
print("The total cost after discount is:", initial_cost)
