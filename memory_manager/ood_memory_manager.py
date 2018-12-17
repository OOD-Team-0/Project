class MemoryManager:
    def __init__(self, memSize):
        self.mainMemory = [x*0 for x in range(memSize)]
        self.runningProcesses = []
        self.mma = None