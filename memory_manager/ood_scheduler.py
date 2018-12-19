from abc import ABC, abstractmethod

class Scheduler(ABC):
    """"
		Interface for an OS Scheduler. 
		:param	ABC
    """
    @abstractmethod
    def getProcessEvents(self): pass
