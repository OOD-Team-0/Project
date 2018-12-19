from tkinter import *
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
        print(self.bar)
