from ood_memory_management_algorithm import MemoryManagementAlgorithm
from ood_memory_event import MemoryEvent

class FirstFit(MemoryManagementAlgorithm):
    def __init__(self): pass

    def addProcess(self, p, mm):
        found = False
        index = -1
        while(not found and index < len(mm)):
            index += 1
            if(mm[index] == 0 and all(x == 0 for x in mm[index:index + p.size])):
                found = True
            else:
                index += p.size - 1

        if(found):
            positions = []
            for i in range(p.size):
                mm[index + i] = p.pid
                positions.append(index + i)

            return MemoryEvent(p.pid, positions)
        return None

    def removeProcess(self, p, mm):
        indexes = [i for i in range(len(mm)) if mm[i] == p.pid]
        return MemoryEvent(p.pid, indexes)