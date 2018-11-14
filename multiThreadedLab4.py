import requests
import threading
from timer import timeit
import json
import copy
import os
import time

ZIP_CODES = [94086, 92093, 90013, 95192, 94132, 94720, 95064, 95819, 92697, 93940, 94544]

DEBUG_VALUE = False #Debug used to manage being blocked from website while testing

SAMPLE_URL = r"https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22" #MTV
API_KEY = "&APPID=3a4d4260edbb76d3c27c71f306b44c9c"


class Weather:
    __slots__ = ['zipCodes', 'cityList', 'weatherInfoDict', 'debug', 'startTime']
    def __init__(self, debug=False, zipCodes:list = ZIP_CODES):
        """Given a list of zipCodes parces weather API into a list of cities and nested dict of attributed keyed by Zipcode"""
        self.debug = True
        self.zipCodes = zipCodes
        urlList = self.updateZipCodes(zipCodes)
        weatherListOfDicts = self.getWeatherInfo(urlList)
        self.cityList, self.weatherInfoDict = self.formatWeatherInfo(weatherListOfDicts)

    def updateZipCodes(self,zip_codes):
        """Given list of zip codes, returns url with mapped route to city"""
        updateUrl = []
        for zipCode in zip_codes:
            # Added units = imperial
            url = r"http://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial".format(zipCode)
            url += API_KEY #concats string
            updateUrl.append(url)

        return updateUrl

    def getWeather(self, url:str, result_data):
        """Given url requests and returns api"""
        page = requests.get(url)
        result_data.append(page.json()) #page.json()

    @timeit
    def getWeatherInfo(self, urlList):
            """ Given urls with appropriate routes, """
            createNewFile = False

            # ```````````````````````````Testing``````````````````````````````````````````````````````
            if self.debug:
                if os.path.isfile("json_output.json"):
                    with open("json_output.json", "r") as read_file:
                        store = json.load(read_file)
                    timeInserted = store[0]["timeInserted"]
                    if time.time() - timeInserted < 1000: # if its less than some time since we collected store values
                        store.pop(0)
                        return store
                    else:
                        createNewFile = True
                else:
                    createNewFile = True

            # `````````````````````````Threading````````````````````````````````````````````````````````
            listOfThreads = []
            resultData = []
            for url in urlList:
                t = threading.Thread(target=self.getWeather, args=(url, resultData))
                t.start()
                listOfThreads.append(t)

            self.joinThreads(listOfThreads)
            print(os.path.basename(__file__))

            # ```````````````````Testing```````````````````````````````````````````````````
            if createNewFile: #if its been a while, re-gather the values
                # From json to json file
                temp = copy.copy(resultData)
                temp.insert(0, {"timeInserted": time.time()})
                with open("json_output.json", "w") as output:
                    json.dump(temp, output, separators=(",", ": "), indent=4)

            return resultData

    def joinThreads(self, allThreads:list):
        """Give list of threads, joins the them together to end processes"""
        for thread in allThreads:
            thread.join()


    def formatWeatherInfo(self, cityData:dict):
        """Given dictionary, extracts a city list and assigns a zipcode as a key to a dictionary of city description and temp """

        cityList = []
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
            city["time created"] = time.time()

        return cityList, cityDict

if __name__ =='__main__':
    w = Weather(debug=DEBUG_VALUE)
        # Stored fetched API's in a file so that we would not be blocked again while testing.

