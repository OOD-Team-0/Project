from abc import ABC, abstractmethod
class MemoryManagementAlgorithm(ABC):
    """
        This abstract class will be implemented by different types of memory allocation algorithms such as first fit, buddy system
        best fit etc
    """

    """
    :param p: Process
    :param mm: Main memory
    :return: indexes at which the process was added to
    """
    @abstractmethod
    def addProcess(self, p, mm): pass

    """
    :param p: Process
    :param mm: Main Memory
    :return: index(es) at which the process was removed
    """
    @abstractmethod
    def removeProcess(self, p, mm): pass