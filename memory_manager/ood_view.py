<<<<<<< HEAD
from tkinter import *
=======
>>>>>>> 85f22a0782c3726371fa2166bbb5136141efc3db
from ood_observer import Observer
from random import randint

class View(Observer):
    # Should be made into GUI
    def __init__(self, size):
        self.bar = [x*0 for x in range(size)]
        self.gui = Tk()
        self.gui.title("Memory Manager")
        self.gui.update()

    def update(self, me):

        added = False
        for i in me.indexes:
            if(self.bar[i] == me.pid):
                self.bar[i] = 0
            else:
                self.bar[i] = me.pid
                added = True
        if(added):
            s = 'Added'
        else:
            s = 'Removed'
        print('Pid:{}, {}:{}'.format(me.pid, s ,me.indexes))
<<<<<<< HEAD
        print(self.bar)
=======
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
    
>>>>>>> 85f22a0782c3726371fa2166bbb5136141efc3db
