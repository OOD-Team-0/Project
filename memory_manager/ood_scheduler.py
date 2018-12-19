from abc import ABC, abstractmethod

class Scheduler(ABC):
    @abstractmethod
    def getProcessEvents(self): pass
