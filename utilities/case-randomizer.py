import random

def randomize(it):
    for i in range(0, len(it)):
        x = random.randint(0,1)
        if x == 1:
            it = it[:i] + it[i].upper() + it[i+1:]
    return it

toRand = "actually for adult, the average is 100"

it = randomize(toRand)
print(it)