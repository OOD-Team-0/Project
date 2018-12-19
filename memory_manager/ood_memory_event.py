class MemoryEvent:
    """
        Whenever a process is added or removed from main memory by the memory manager, a memory event will be created for record
    """
    def __init__(self, pid, indexes):
        """
        MemoryEvent Constructor
        :param pid: id of the process that has been affected in main memory
        :param indexes: index(es) in array that have been affected in main memory
        """
        self.pid = pid
        self.indexes = indexes
