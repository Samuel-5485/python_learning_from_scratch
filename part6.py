# Comparation program
x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x==y:
    print("x is equal to y")

# if-elif
# Logic for <,>,==
if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
elif x==y:
    print("x is equal to y")
# Logic OR
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Logic for !=
if x!=y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# a program that accept score from student then display their grade
score = float(input("Enter your score: "))
if score >= 90 and score <= 100:
    print("Your grade is A+")
elif score >= 80 and score < 90:
    print("Your grade is A")
elif score >= 70 and score < 80:
    print("Your grade is B")
elif score >= 60 and score < 70:
    print("Your grade is C")
elif score >= 50 and score < 60:
    print("Your grade is D")
else:
    print("Your grade is F")

# write a program that accepts number from user and prints either even or odd
num = int(input("Enter a number: "))
if num%2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number") 

def main():
    num = int(input("Enter a number: "))
    if is_even(num):
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

main()