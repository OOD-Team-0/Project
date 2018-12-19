from ood_observable import Observable
from time import sleep
'''
TODO
'''
class OS(Observable):

    def __init__(self):
        super().__init__()
        self.memManager = None
        self.scheduler = None

    def setMemoryManager(self, memMan):
        self.memManager = memMan

    def setScheduler(self, sched):
        self.scheduler = sched

    def setView(self, v):
        self.view = v
        self.view.setBarSize(len(self.memManager.mainMemory))

    def run(self):
        processes = self.scheduler.getProcessEvents()
        for p in processes:
            me = self.memManager.handleProcess(p)
            if(me):
                self.notifyObservers(me)


