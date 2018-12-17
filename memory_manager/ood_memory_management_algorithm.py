from abc import ABC, abstractmethod

class MemoryManagementAlgorithm(ABC):
    @abstractmethod
    def addProcess(self, p, mm): pass

    @abstractmethod
    def removeProcess(self, p, mm): pass