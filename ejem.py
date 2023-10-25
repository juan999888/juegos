import random

red=1

blue=2

green=3

color=[red,blue,green]
for i in range (3):

    e=random.choice(color)
    print(e)
    n=color.index(e)
    color.pop(n)
    
