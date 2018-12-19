from abc import ABC, abstractmethod

class Observer(ABC):
    """
		Interface for an Observer. 
		Classes that intend on listening for updates from other classes
		should use the Observer interface.
		:param	ABC
    """
    @abstractmethod
    def update(self, object): pass

