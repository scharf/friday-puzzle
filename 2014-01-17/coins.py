import random


# totoal number of exxperiments
tot = 0
# experiments that we accept (because we see Head)
accepted = 0
# the number of thimes the other coin was Head
head = 0

# this is our coin
class Coin:
    def __init__(self, *sides):
        self.sides = sides

    def roll(self):
        "throw the coin"
        self.face = random.choice(self.sides)

# the coins we use
coins = [Coin('Head', 'Head'), Coin('Head', 'Tail')]

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
    # we only look at cases where the coin is Head!
    if side == 'Head':
        # "...It's a head...."
        # this is an accepted outcome (we ignore the other outcomes)
        accepted += 1
        # "...What's the probability that the other side also contains a head?"

        # look at the other coin
        other_coin = box_with_coins[0]
        # and count the number of heads
        if other_coin.face == 'Head':
            head += 1

# finally we calculate the probability
probability_percent = (100. * head / accepted)

print "the experiment was done %(tot)d times but we accepted only %(accepted)d cases where the coin was Head" % globals()
print "The probability of Head = %(probability_percent).1f%%" % globals()
