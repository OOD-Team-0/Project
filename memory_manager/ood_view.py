
from random import randint


def randomAction(a):
    searching = True
    while(searching):
        i = randint(0,3)
        if(a[i] != None):
            searching = False
    return i

b = [1,1,None,1]

for i in range(50):
    print(randomAction(b))
    
