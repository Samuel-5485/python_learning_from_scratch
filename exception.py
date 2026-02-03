# Exception
try:
    x = int(input("What's x? "))
    # print(f"x is {x}")
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
# print(f"x is {x}") #NameError: name 'x' is not defined

#  Exception handling: function, break
def main():
    y = get_int()
    print(f"y is {y}")

def get_int():
    while True:
        try:
            y = int(input("What's y? "))
        except ValueError:
            print("y is not integer")
        else:
            break
    return y
main()

# Exception handling: function, pass
def main():
    z = get_int("What's z? ")
    print(f"z is {z}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        
main()