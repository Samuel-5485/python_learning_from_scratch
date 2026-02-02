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





