'''
Sarah
Hieu

'''

import requests
from timer import timeit
import os
DEBUG_VALUE = False

ZIP_CODES = [94086, 92093, 90013, 95192, 94132, 94720, 95064, 95819, 92697, 93940, 94544]
SAMPLE_URL = r"https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22"
API_KEY = "&APPID=3a4d4260edbb76d3c27c71f306b44c9c"


class Weather:
    __slots__ = ['zipCodes', 'cityList', 'weatherInfoDict'] # creates space in memory to increase optimization
    def __init__(self, zipCodes:list):
        """Given a list of zipCodes parces weather API into a list of cities and nested dict of attributed keyed by zipcode"""
        self.zipCodes = zipCodes
        urlList = self.updateZipCodes(zipCodes)
        weatherDict = self.getWeatherInfo(urlList)
        self.cityList, self.weatherInfoDict = self.formatWeatherInfo(weatherDict)

    def updateZipCodes(self, zip_codes):
        """Given list of zip codes, returns url with mapped route to city"""
        updateUrl = []
        for zipCode in zip_codes:
            url = r"http://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial".format(zipCode)
            url += API_KEY #concats string
            updateUrl.append(url)
        return updateUrl


    def getWeather(self, url:str):
        """Given url requests and returns api"""
        page = requests.get(url)
        return page.json()

    @timeit
    def getWeatherInfo(self, urlList):
        """ Given a list of urls, calls list"""

        weatherDicts = []
        for url in urlList:
            cityWeatherDict = self.getWeather(url)
            weatherDicts.append(cityWeatherDict)

        print(os.path.basename(__file__))

        return weatherDicts

    def formatWeatherInfo(self, cityData:dict):
        """Given dictionary, extracts a city list and assigns a zipcode as a key to a dictionary of city description and temp """
        cityList = []
        index = 0
        cityDict = {}

        for city in cityData:
            cityName = city.get("name")
            cityList.append(cityName)
            D = {}
            L = city.get("main")
            D['temp'] = L.get('temp')
            L = city.get("weather")
            weatherDict = L[0]
            D['description'] = weatherDict.get('description')
            cityDict[cityName] = D

        return cityList, cityDict

if __name__ =='__main__':
    w = Weather(ZIP_CODES)

