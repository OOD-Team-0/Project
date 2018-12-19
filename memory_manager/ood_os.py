from ood_observable import Observable
from time import sleep

class OS(Observable):
    """
        Opearating System, responsible for tasks such as scheduling processes,
        managing main memory and updating the view with essential data
    """
    def __init__(self):
        """
        OS Constructor
        :field memManager: Memory Manager that the OS will be using
        :field scheduler: scheduler that the OS will be using
        """
        super().__init__()
        self.memManager = None
        self.scheduler = None
        self.view = None

    def setMemoryManager(self, memMan):
        """
        :param memMan: taking in a memory manager and setting it to this specified memory manager
        :return: none
        """
        self.memManager = memMan

    def setScheduler(self, sched):
        """
        :param sched: taking in a scheduler and setting it to this specified scheduler
        :return:
        """
        self.scheduler = sched

    def setView(self, v):
        """
        :param v: taking in a view and setting it to this specified view
        :return:
        """
        self.view = v
        self.view.setBarSize(len(self.memManager.mainMemory))

    def run(self):
        """
        Getting all process events from the process scheduler
        Giving all process to the memory manager to handle
        Notifying all observers listening for updates from the OS
        :return: none
        """
        processes = self.scheduler.getProcessEvents()
        for p in processes:
            me = self.memManager.handleProcess(p)
            if(me):
                self.notifyObservers(me)


