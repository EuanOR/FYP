import json
import requests


class WeatherAPI(object):

    def __init__(self, lat="51.903614", lon="-8.468399"):
        self._lat = lat
        self._lon = lon
        self._unit = "metric"
        self._app_id = "fb59b4d9d9a9c3fa5ce7747f8c17a780"
        self._url = \
            ("http://api.openweathermap.org/data/2.5/weather?lat="
             + self._lat +
             "&lon=" + self._lon +
             "&units=" + self._unit +
             "&APPID=" + self._app_id)
        self._json = self.requestAPI()

    def requestAPI(self):
        r = requests.get(self._url)
        return r.json()

    def get_temperature(self):
        temperature = self._json['main']['temp']
        return temperature

    def get_humidity(self):
        humidity = self._json['main']['humidity']
        return humidity

    def get_town(self):
        town = self._json['name']
        return town


def test():
    w = WeatherAPI("-37.8136", "144.9631")
    print(w._url)
    print(w._json)
    print(w.get_temperature())
    print(w.get_humidity())
    print(w.get_town())


if __name__ == "__main__":
    test()
