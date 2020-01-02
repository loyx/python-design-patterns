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


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.observable = weather_data
        self.observable.registerObserver(self)
        self.max_temperature = -0x3f3f3f
        self.min_temperature = 0x3f3f3f
        self.avg_temperature = 0
        self.__cont_record = 0

    def update(self):
        curr_temperature = self.observable.getTemperature()
        if curr_temperature > self.max_temperature:
            self.max_temperature = curr_temperature
        if curr_temperature < self.min_temperature:
            self.min_temperature = curr_temperature
        self.avg_temperature = (self.avg_temperature * self.__cont_record +
                                curr_temperature) / (self.__cont_record+1)
        self.__cont_record += 1
        self.display()

    def display(self):
        print("Avg/Max/Min temperature:{}/{}/{}".format(
            self.avg_temperature,
            self.max_temperature,
            self.min_temperature
        ))
