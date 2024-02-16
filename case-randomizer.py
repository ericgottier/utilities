import random

def randomize(it):
    for i in it:
        x = random.randint(0,1)
        if x == 1:
            it = it.replace(i, i.upper(), 1)
    return it

it = randomize("Why can't i afford nintendo internet???")
print(it)