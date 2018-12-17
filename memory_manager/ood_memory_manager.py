class MemoryManager:
    def __init__(self, memSize):
        self.mainMemory = [x*0 for x in range(memSize)]
        self.runningProcesses = []
        self.mma = None

    def setMMA(self, mma):
        self.mma = mma

    def handleProcess(self, p):
        if(p not in self.runningProcesses):
            self.runningProcesses.append(p)
            return self.addProcess(p)
        else:
            return self.removeProcess(p)


    def addProcess(self, p):
        self.runningProcesses.remove(p)
        return self.mma.addProcess(p, self.mainMemory)

    def removeProcess(self, p):
        return self.mma.removeProcess(p, self.mainMemory)