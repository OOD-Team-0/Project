from ood_scheduler import Scheduler
from time import time
from random import randint
from ood_process import Process


class FakeScheduler(Scheduler):

    def __init__(self):
        self.MIN_SIZE = 1
        self.MAX_SIZE = 5
        self.MIN_TIME = 2
        self.MAX_TIME = 5

        self.id = 1

        self.processes = []
        self.interval = 1

        self.timeToGen = time()

    def getProcessEvents(self):
        sendProcesses = []
        for p in self.processes:
            if(time() > p.endTime):
                sendProcesses.append(p)
        if(time() > self.timeToGen):
            proc = self.generateProcess()
            sendProcesses.append(proc)
            self.processes.append(proc)
            self.timeToGen = self.generateTime()
        return sendProcesses

    def generateTime(self):
        return time() + self.interval

    def generateProcess(self):
        p = Process(self.id, self.genProcessSize(), self.genProcessTime())
        self.id += 1
        return p

    def genProcessSize(self):
        return randint(self.MIN_SIZE, self.MAX_SIZE + 1)

    def genProcessTime(self):
        return time() + randint(self.MIN_TIME, self.MAX_TIME + 1)