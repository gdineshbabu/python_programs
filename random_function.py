# random function

import random as r
l=[10,20,30,40]
print(random.choice(l))
print(random.choices(l,k=2))
print(r.randrange(10,25,2))
print(r.random())
r.shuffle(l)
print(l)
r.uniform(10,15)
