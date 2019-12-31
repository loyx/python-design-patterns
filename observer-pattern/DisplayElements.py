from ObserverPattern import Observer, DisplayElement


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.observable = weather_data
        self.observable.registerObserver(self)
        self.temperature = weather_data.getTemperature()
        self.humidity = weather_data.getHumidity()

    def update(self):
        self.temperature = self.observable.getTemperature()
        self.humidity = self.observable.getHumidity()
        self.display()

    def display(self):
        print("Current conditions:{}F degrees and {}% humidity".
              format(self.temperature, self.humidity))

