class Observable:
    """
    Subject(Observable) class, observers can register with this subject and receive all updated data
    """
    def __init__(self):
        """
        Observable Constructor
        :field observers: list of observers
        :field changed: state of the subject(observable)
        """
        self.observers = []
        self.changed = False

    def addObserver(self, observer):
        """
        :param observer: observer to be added to the observable's list of observers
        :return: none
        """
        if not observer in self.observers:
            self.observers.append(observer)

    def setChanged(self):
        """
        setting the state of the observable true, the observable has changed
        :return: none
        """
        self.changed = True

    def clearChanged(self):
        """
        will be called after notifying all observers
        sets the status of the observable to false, it has not changed
        :return: none
        """
        self.changed = False

    def hasChanged(self):
        """
        :return: the current status of the observable
        """
        return self.changed

    def deleteObserver(self, observer):
        """
        :param observer: the observer to be removed from the observable's list of observers
        :return: none
        """
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notifyObservers(self, subject):
        """
        :param subject: will update all observers that are listening to this subject(observable)
        :return: none
        """
        if(subject):
            for observer in self.observers:
                observer.update(subject)
            self.clearChanged()