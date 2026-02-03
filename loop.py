# Loop in python
# While loop
i = 3
while i != 0:
    print("Python")
    i -= 1 #decrement

i = 1
while i <= 4:
    print("Learning together!")
    i += 1

# For loop
for _ in range(3): #why we don't use i instead of _
    print("Python")

while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("Learn")

def main():
    number = get_number()
    python(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def python(n):
    for _ in range(n):
        print("Python")
main()

# List
students = ['Sami', 'Harry', 'Cherry']
for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])

# Dictionary
students = {
    "Python": "language",
    "Vscode": "code editor",
    "Github": "sourse code storage"
}
print(students["Python"])
print(students["Vscode"])
print(students["Github"])

for student in students: 
    print(student, students[student], sep=", ")  #sep means space
# dict2
students = [
    {
        "name": "Alice", 
        "house": "Sheger",
        "job": "developer"
    },
    {
        "name": "Cherry",
        "house": "Addis Ababa",
        "job": "Ai enginner"
    }

]
for student in students:
    print(student["name"], student["house"], student["job"], sep=", ")

# column
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

# row
def main():
    print_row(3)

def print_row(width):
    print("*" * width)

main()
# square
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("*" * size)
main()