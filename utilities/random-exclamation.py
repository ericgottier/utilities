import random

chars = ['!', '?', '1']

excl = ''
for i in range(random.randint(7, 50)):
    choose = random.randint(0,2)
    excl += chars[choose]

print(excl)