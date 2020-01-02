class Observable:

    def __init__(self):
        self._changed = True
        self._observers_list = []

    def registerObserver(self, observer):
        if observer not in self._observers_list:
            self._observers_list.append(observer)

    def removeObserver(self, observer):
        if observer in self._observers_list:
            self._observers_list.remove(observer)

    def notifyObserver(self):
        if self._changed:
            for observer in self._observers_list:
                observer.update()

    def setChanged(self):
        self._changed = True

    def clearChanged(self):
        self._changed = False

    def hasChanged(self):
        return self._changed


class Observer:

    def update(self):
        pass


class DisplayElement:

    def display(self):
        pass
