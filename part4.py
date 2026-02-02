# While loop syntax and exercise soln
"""
names =[]
while True:
    name = input("Enter student name")
    if name == "stop":
        break
    names.append(name)

i = 0
while i<len(names):
    print("Student", i, " =", names[i])
    i = i+1
    """
# Loop statements
# While Loops: is used to execute a block of code repeatedly as long as a given condition is true.
i = 1
while i<=4:
    print(i)
    i = i + 1

# check the following conditions
a = 1
while a < 10:
    print(a)
    a = a + 2

# use while loop to print all natural numbers between 1 to 100
i = 1
while i <= 100:
    print(i)
    i = i+1

#  calculate the of the sum of all the elements in alist
numbers = [1,2,3,4,5]
sum = 0
i = 0
while i < len(numbers):
    sum = sum + numbers[i]
    i = i+1
print("Sum =", sum)

""" white a program that accepts the names of n students and
 then display their name.
  Hint: The total number of student should be provided by the user"""
n = int(input("Enter the total number of students: "))
student_names = []
i = 0
while i < n:
    name = input("Enter the name of student " + str(i))
    student_names.append(name)
    i = i + 1

i = 0
while i<len(student_names):
    print("### STUDENT DATABASE")
    print(student_names[i])
    i = i+1

student_names=[]
while True:
    name = input("Student name")
    if name == 'x':
        break
    student_names.append(name)
print("#list of students")
i = 0
while i<len(student_names):
    print(student_names[i])
    i+=1