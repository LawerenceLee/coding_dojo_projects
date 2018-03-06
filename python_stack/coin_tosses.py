import random


def coin_tosses():
    print("Starting the program...")
    tails = 0
    heads = 0
    for x in range(1, 5001):
        coin = random.random()
        if coin > 0.5:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and () tail(s) so far".format(x, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and () tail(s) so far".format(x, heads, tails))
    print("Ending the program, thank you!")


coin_tosses()
