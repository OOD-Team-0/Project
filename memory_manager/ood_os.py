from ood_memory_manager import MemoryManager
from ood_scheduler import Scheduler
from ood_view import View
from time import sleep
'''
TODO
'''


class OS:

    def __init__(self):
        self.memManager = None
        self.scheduler = None
        self.view = None

    def setMemoryManager(self, memMan):
        self.memManager = memMan

    def setScheduler(self, sched):
        self.scheduler = sched

    def setView(self, v):
        self.view = v
        self.view.setBarSize(len(self.memManager.mainMemory))

    def run(self):
        print('running')
        while(True):
            processes = self.scheduler.getProcessEvents()
            for p in processes:
                me = self.memManager.handleProcess(p)
                self.view.update(me)
            sleep(0.5)