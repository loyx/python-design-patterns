from ObserverPattern import Observable


class WeatherData(Observable):

    def __init__(self):
        super().__init__()
        self.__temperature = 0
        self.__humidity = 0
        self.__pressure = 0

    def measurementChanged(self):
        self.setChanged()
        self.notifyObserver()

    def setMeasurements(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurementChanged()

    def getTemperature(self):
        return self.__temperature

    def getHumidity(self):
        return self.__humidity

    def getPressure(self):
        return self.__pressure
