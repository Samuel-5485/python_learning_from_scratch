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