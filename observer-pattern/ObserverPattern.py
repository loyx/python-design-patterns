class Observable:

    def __init__(self):
        self._observers_list = []

    def registerObserver(self, observer):
        if observer not in self._observers_list:
            self._observers_list.append(observer)

    def removeObserver(self, observer):
        if observer in self._observers_list:
            self._observers_list.remove(observer)

    def notifyObserver(self):
        for observer in self._observers_list:
            observer.update()


class Observer:

    def update(self):
        pass


class DisplayElement:

    def display(self):
        pass
