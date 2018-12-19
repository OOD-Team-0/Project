from ood_memory_event import MemoryEvent

class MemoryManager:
    def __init__(self, memSize):
        self.mainMemory = [x*0 for x in range(memSize)]
        self.processQueue = []
        self.mma = None


    def setMMA(self, mma):
        self.mma = mma

    def handleProcess(self, p):
        if(p.pid not in self.mainMemory):
            return self.addProcess(p)
        else:
            return self.removeProcess(p)


    def addProcess(self, p):
        if(p in self.processQueue):
            self.processQueue.remove(p)
        posistions = self.mma.addProcess(p, self.mainMemory)
        if(posistions):
            for i in posistions:
                self.mainMemory[i] = p.pid
            return MemoryEvent(p.pid, posistions)
        else:  # not enough room
            self.processQueue.append(p)
            return None


    def removeProcess(self, p):
        positions = self.mma.removeProcess(p, self.mainMemory)
        for i in positions:
            self.mainMemory[i] = 0
        if(len(self.processQueue) > 0):
            for p in self.processQueue:
                self.addProcess(p)
        return MemoryEvent(p.pid, positions)