import random 
import statistics
import sys
import cowsay

"""
coin = random.choice(["heads", "tails"])
print(coin)
"""
# random.randint
# number = random.randint(1, 9)
# print(number)

#random.shuffle
"""
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
"""
#take a look docs.python.org/3/library/statistics.html
# print(statistics.mean([40, 30]))
"""
try:
    print("hey, welcome to learn with me!", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""
#Check for errors
"""
if len(sys.argv) < 2:
    # print("Too few arguments")
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    # print("Too many arguments")
    sys.exit("Too many arguments")
# else:

print("hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1: ]:
    print("hello, my name is", arg)
"""
if len(sys.argv) == 2:
    print(cowsay.cowsay("hey, " + sys.argv[1]))

# name = " ".join(sys.argv[1:])
# print(cowsay.cowsay(f"hey, {name}"))