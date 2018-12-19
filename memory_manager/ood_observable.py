class Observable:

    def __init__(self):
        self.observers = []
        self.changed = False

    def addObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def setChanged(self):
        self.changed = True

    def clearChanged(self):
        self.changed = False

    def hasChanged(self):
        return self.changed

    def deleteObserver(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notifyObservers(self, subject):
        if(subject):
            for observer in self.observers:
                observer.update(subject)
            self.clearChanged()