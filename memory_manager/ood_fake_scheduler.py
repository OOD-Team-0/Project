from ood_scheduler import Scheduler
from ood_process import Process
from time import time
from random import randint

class FakeScheduler(Scheduler):
    """
		A specific scheduler to simulate process creation.
    """
    def __init__(self):
        """
			Constructor for the FakeScheduler.
			Sets min/max size and time of processes.
			Creates list of processes.
			param: self
        """
        self.MIN_SIZE = 2
        self.MAX_SIZE = 10
        self.MIN_TIME = 5
        self.MAX_TIME = 15

        self.id = 1

        self.processes = []
        self.interval = 1

        self.timeToGen = time()

    def getProcessEvents(self):
        """
			If a list of processes has been created but not sent to the OS, send them.
			Remove all processes being sent from the 'processes' list.
			:param	self
			:return	processes to send to OS
        """
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
        """
			Specifies time it takes to generate a process.
			:param	self
			:return	process generation time
        """
        return time() + self.interval

    def generateProcess(self):
        """
			Create a new, "randomized" process to be sent to the OS.
			:param	self
			:return	process
        """
        p = Process(self.id, self.genProcessSize(), self.genProcessTime())
        self.id += 1
        return p

    def genProcessSize(self):
        """
			Generate a 
			:param	self
        """
        return randint(self.MIN_SIZE, self.MAX_SIZE)

    def genProcessTime(self):
        """
			
			:param	self
        """
        return time() + randint(self.MIN_TIME, self.MAX_TIME + 1)