import random 
import statistics
"""
coin = random.choice(["heads", "tails"])
print(coin)
"""
# random.randint
number = random.randint(1, 9)
print(number)

#random.shuffle
"""
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
"""
#take a look docs.python.org/3/library/statistics.html
print(statistics.mean([40, 30]))