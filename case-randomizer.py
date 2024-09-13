import random

def randomize(it):
    for i in range(0, len(it)):
        x = random.randint(0,1)
        if x == 1:
            it = it[:i] + it[i].upper() + it[i+1:]
    return it

toRand = "Who here is excited for 20 minutes of civ 7 gameplay at 4:30 est"

it = randomize(toRand)
print(it)