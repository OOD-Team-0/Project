from ood_memory_management_algorithm import MemoryManagementAlgorithm


class FirstFit(MemoryManagementAlgorithm):
    """
     First fit allocation algorithm, a process is allocated into main memory in the first sufficient index(es)
     starting from the beginning of Main Memory
    """

    def __init__(self): pass

    def addProcess(self, id, size, mm):
        """
        :param p: Process
        :param mm: Main memory
        :return: indexes at which the process was added to
        """
        found = False
        index = -1
        while(not found and index < len(mm)):
            index += 1
            if(mm[index] == 0):
                if((index + size < len(mm)) and all(x == 0 for x in mm[index:index + size])):
                    found = True
                else:
                    index += size - 1
        if(found):
            positions = []
            for i in range(size):
                mm[index + i] = id
                positions.append(index + i)

            return positions
        return None

    def removeProcess(self, id, size, mm):
        """
        :param p: Process
        :param mm: Main Memory
        :return: index(es) at which the process was removed
        """
        return [i for i in range(len(mm)) if mm[i] == id]

