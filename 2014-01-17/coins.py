import random


tot      = 0
accepted = 0
head     = 0

# this is our coin
class Coin:
    def __init__(self,*sides):
        self.sides = sides
    def roll(self):
        "throw the coin"
        self.face = random.choice(self.sides)

# the coins we use
coins = [Coin('H','H'), Coin('H','T')]


for i in range(10000):
    tot += 1
    # put the cons in the box (copy the array)
    box_with_coins = coins[:]

    # shake our coins
    for coin in box_with_coins:
        coin.roll()

    # "You take one of the coins out of the box..."
    selected_coin = random.choice(box_with_coins)
    box_with_coins.remove(selected_coin)
    # "...and look at one of the sides..."
    side = selected_coin.face
    # we ignore cases when it is not head
    if side == 'H':
        # "...It's a head...."
        # this is an accepted outcome (we ignore the other outcomes)
        accepted += 1
        # "...What's the probability that the other side also contains a head?"

        # take the other coin
        other_coin = box_with_coins[0]
        # and count th number of heads
        if other_coin.face == 'H':
            head += 1
probability_percent = (100.*head/accepted)

print "the experiment was done %(tot)d times but we accepted only %(accepted)d cases where the coin was H" % globals()
print "The probability of Head = %(probability_percent).1f%%" % globals()
