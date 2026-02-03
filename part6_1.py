name = str(input("Enter your name: "))
if name == "Alice" or name == "alice":
    print("Hello, Alice!")
elif name == "Bob" or name == "bob":
    print("Hello, Bob!")
elif name == "Charlie" or name == "charlie":
    print("Hello, Charlie!")
else:
    print("Hello, stranger!")

match name:
    case "Alice" | "alice":
        print("Hello, Alice!")
    case "Bob" | "bob":
        print("Hello, Bob!")
    case _:  #default
        print("Hello, stranger!")