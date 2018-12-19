from ood_memory_event import MemoryEvent

class MemoryManager:
    """
		Manages main memory based on specifications from a MemoryManagementAlgorithm (MMA).
		MemoryManager sends references to main memory, processes, and a process queue to MMA
		in order to allow the MemoryManagementAlgorithm to modify the values appropriately.
    """
	
    def __init__(self, memSize):
        """
			Constructor for the MemoryManager.
			Builds main memory based on specified memory size.
			Creates process queue to hold processes that come in from OS.
			:param	self
			:param	memSize
        """
        self.mainMemory = [x*0 for x in range(memSize)]
        self.processQueue = []
        self.mma = None

    def setMMA(self, mma):
        """ Sets the value of the MemoryManagementAlgorithm. """
        self.mma = mma

    def handleProcess(self, p):
        """
			Handles an incoming process accordingly, based on mainMemory and processQueue.
			:param	self
			:param	p
			:return	MemoryEvent, if process is in mainMemory then remove, else add process to mainMemory.
        """
        if(p.pid not in self.mainMemory):
            return self.addProcess(p)
        else:
            return self.removeProcess(p)


    def addProcess(self, p):
        """
			If process (p) is in processQueue, remove.
			Add process to mainMemory according to memoryManagementAlgorithm.
			If not enough room in mainMemory, add process to processQueue.
			:param	self
			:param	p
			:return	MemoryEvent
        """
        if(p in self.processQueue):
            self.processQueue.remove(p)
        positions = self.mma.addProcess(p, self.mainMemory)
        if(positions):
            for i in positions:
                self.mainMemory[i] = p.pid
            return MemoryEvent(p.pid, positions)
        else:  # not enough room
            self.processQueue.append(p)
            return None


    def removeProcess(self, p):
        """
			Remove process from mainMemory according to memoryManagementAlgorithm.
			Then, attempt to add processes from the processQueue into mainMemory.
			:param	self
			:param	p
			:return	MemoryEvent
        """
        positions = self.mma.removeProcess(p, self.mainMemory)
        for i in positions:
            self.mainMemory[i] = 0
        if(len(self.processQueue) > 0):
            for p in self.processQueue:
                self.addProcess(p)
        return MemoryEvent(p.pid, positions)