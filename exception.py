# Exception
try:
    x = int(input("What's x? "))
    # print(f"x is {x}")
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
# print(f"x is {x}") #NameError: name 'x' is not defined

while True:
    try:
        y = int(input("What's y? "))
    except ValueError:
        print("y is not integer")
    else:
        break
print(f"y is {y}")