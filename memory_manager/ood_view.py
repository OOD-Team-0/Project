
from random import randint

class View:
    # Should be made into GUI
    def __init__(self):
        self.bar = []

    def setBarSize(self, size):
        self.bar = [x*0 for x in range(size)]

    def update(self, me):
        print('Pid:{}, Is:{}'.format(me.pid, me.indexes))
        for i in me.indexes:
            if(self.bar[i] == me.pid):
                self.bar[i] = 0
            else:
                self.bar[i] = me.pid
        print(self.bar)


#def randomAction(a):
    #searching = True
    #while(searching):
        #i = randint(0,3)
        #if(a[i] != None):
            #searching = False
    #return i

#b = [1,1,None,1]

#for i in range(50):
   # print(randomAction(b))
    
