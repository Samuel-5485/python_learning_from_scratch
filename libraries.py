import random 
"""
coin = random.choice(["heads", "tails"])
print(coin)
"""
# random.randint
number = random.randint(1, 9)
print(number)

#random.shuffle
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)