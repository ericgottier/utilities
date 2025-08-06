import random

chars = ['!', '?', '1', '']

collect_chars = []
for i in range(random.randint(7, 500000)):
    choose = random.randint(0,len(chars)-1)
    collect_chars.append(chars[choose])
    
excl = ''.join(collect_chars)

print(excl)