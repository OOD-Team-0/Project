from tkinter import *
from tkinter.ttk import *
from ood_observer import Observer
from random import randint
from time import sleep

class View(Observer):
    # Should be made into GUI
    def __init__(self, size):
        self.bar = [x*0 for x in range(size)]
        self.gui = Tk()
        self.gui.title("Memory Manager")
        self.gui.geometry("500x500")
        # Label
        self.progressBarLabel = Label(self.gui, text="Total Memory")
        self.progressBarLabel.pack(padx=10, pady=10)
        # ProgessBar
        self.progressNum = IntVar()
        self.progressBar = Progressbar(self.gui,orient=HORIZONTAL,length=100,mode='determinate', variable=self.progressNum)
        self.progressBar.pack(fill=X, padx=10, pady=10)
        # Percentage Label
        self.percentageString = StringVar()
        self.percentageString.set('0 % Used')
        self.percentageLabel = Label(self.gui, textvariable=self.percentageString)
        self.percentageLabel.pack(padx=10, pady=10)

        # Start showing
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
        self.updateProgressBar()

    def updateProgressBar(self):
        totalSize = len(self.bar)
        spacesUsed = 0
        # In case size changes over 100, do percentage calc then make it an int again
        for i in self.bar:
            if i != 0:
                spacesUsed = spacesUsed + 1
        percentage = spacesUsed/totalSize
        pbValue = int(percentage*100)
        self.progressNum.set(pbValue)
        self.percentageString.set(str(pbValue) + ' % Used')
        self.gui.update_idletasks()
        sleep(1)


