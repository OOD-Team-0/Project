from tkinter import Tk, Label, IntVar, StringVar, HORIZONTAL, X, Canvas, Button, PhotoImage
from tkinter.ttk import Progressbar
from ood_observer import Observer
from random import randint
from time import sleep

class View(Observer):
    # Should be made into GUI
    def __init__(self, size):
        self.bar = [x*0 for x in range(size)]
        self.gui = Tk()
        self.gui.title("Memory Manager")
        self.gui.geometry("750x350")
        self.gui.iconbitmap("ram.ico")
        # Label
        self.progressBarLabel = Label(self.gui, text="Total Memory: " + str(size), font=("Roboto", 14))
        self.progressBarLabel.pack(padx=10, pady=10)
        # ProgessBar
        self.progressNum = IntVar()
        self.progressBar = Progressbar(self.gui,orient=HORIZONTAL,length=100,mode='determinate', variable=self.progressNum)
        self.progressBar.pack(fill=X, padx=10, pady=10)
        # Percentage Label
        self.percentageString = StringVar()
        self.percentageString.set('0 % Used')
        self.percentageLabel = Label(self.gui, textvariable=self.percentageString, font=("Roboto", 14))
        self.percentageLabel.pack(padx=10, pady=10)
        # Rectangle for Memory
        self.canvas = Canvas(self.gui, width=706, height=50)
        self.canvas.pack()
        self.rectangle = self.canvas.create_rectangle(0,0,706,50,fill='green')

        self.memoryButtons = {}
        self.photo = PhotoImage(file="FFFFFF-0.png")
        self.MAXWIDTH = 700
        self.HEIGHT = 43
        self.STARTX=22
        self.Y=140
        # Test Button
        
        self.testButton1 = Button(self.gui, image=self.photo)
        self.testButton1['width']=self.MAXWIDTH
        self.testButton1['height']=self.HEIGHT
        self.testButton1.place(x=self.STARTX, y=self.Y)

        # #Process Label
        self.processString = StringVar()
        self.processLabel = Label(self.gui, textvariable=self.processString, font=("Roboto", 14))
        self.processLabel.pack(padx=10, pady=(50,0))
        # Size Label
        self.sizeString = StringVar()
        self.sizeLabel = Label(self.gui, textvariable=self.sizeString)
        self.sizeLabel.pack()
        

        # Active Processes Label
        self.activeString = StringVar()
        self.activeLabel = Label(self.gui, textvariable=self.activeString, font=("Roboto", 14))
        self.activeLabel.pack(padx=10, pady=10)

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
        self.updateLabels(me.pid, s, me.indexes)
        self.updateButtons(me.indexes, added, me.pid)
        self.activeProcesses()
        self.updateProgressBar()
        

    def updateProgressBar(self):
        # Fix for weird label glitch
        self.percentageString.set('                                                                                     ')
        self.gui.update_idletasks()

        totalSize = len(self.bar)
        spacesUsed = 0
        # In case size changes over 100, do percentage calc then make it an int again
        for i in self.bar:
            if i != 0:
                spacesUsed = spacesUsed + 1
        percentage = spacesUsed/totalSize
        pbValue = int(percentage*100)
        
        # Update GUI
        self.progressNum.set(pbValue)
        self.percentageString.set(str(pbValue) + ' % Used')
        self.gui.update_idletasks()
        sleep(1)

    def updateLabels(self, pid, action, sizeArray):
        #clear the old strings
        self.processString.set('                                                                                     ')
        self.sizeString.set('                                                                                     ')
        self.gui.update_idletasks()

        if action == 'Added':
            word = 'to'
        else:
            word = 'from'
        self.processString.set(action + ' Process with ID: ' + str(pid) + ' ' + word + ' Memory')

        size = len(sizeArray)

        # Update GUI
        self.sizeString.set('Size: ' + str(size))
        self.gui.update_idletasks()

    def activeProcesses(self):
        #clear the old strings
        self.activeString.set('                                                                                     ')
        self.gui.update_idletasks()

        # Change to set (Removes dupes) - also remove 0 (means nothing is there)
        barAsSet = set(self.bar)
        barAsSet.remove(0)

        if len(barAsSet) == 0:
            barAsSet = 'None'

        # Update GUI
        uniqueProcesses = 'Active Processes: ' + str(barAsSet)
        self.activeString.set(uniqueProcesses)
        self.gui.update_idletasks()

    def updateButtons(self, indexes, whatToDo, pid):
        firstIndex = indexes[0]
        scale = self.MAXWIDTH / 100
        if whatToDo:
            # Have to add a button
            print('here')
            b = Button()
            # Test Button
            # Things you will need
            bWidth = scale * len(indexes)
            bStartX = self.STARTX + (firstIndex * scale)
            b = Button(self.gui, image=self.photo,bg='red')
            b['width']=bWidth
            b['height']=self.HEIGHT
            b.place(x=bStartX,y=self.Y)
            self.gui.update()
            self.memoryButtons[pid]=b
            print(str(self.memoryButtons))
        else:
            b = self.memoryButtons.get(pid)
            del self.memoryButtons[pid]
            print(str(self.memoryButtons))
            b.destroy()
            self.gui.update()



