from ood_scheduler import Scheduler
from ood_process import Process
from time import time
from random import randint


class FakeScheduler(Scheduler):

    def __init__(self):
        self.MIN_SIZE = 1
        self.MAX_SIZE = 10
        self.MIN_TIME = 1
        self.MAX_TIME = 10

        self.id = 1

        self.processes = []
        self.interval = 1

        self.timeToGen = time()

    def getProcessEvents(self):
        sendProcesses = []
        for p in self.processes:
            if(time() > p.endTime):
                sendProcesses.append(p)
        for p in sendProcesses:
            self.processes.remove(p)
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