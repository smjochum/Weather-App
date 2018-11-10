import requests
import threading

import time
import multiprocessing as mp



ZIP_CODES = [94086, 92093, 90013, 95192, 94132, 94720, 95064, 95819, 92697, 93940, 94544]

SAMPLE_URL = r"https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22" #MTV

API_KEY = "&APPID=3a4d4260edbb76d3c27c71f306b44c9c"

class Weather:
    __slots__ = ['zipCodes', 'cityList', 'weatherInfoDict']
    def __init__(self, zipCodes:list):
        """Given a list of zipCodes parces weather API into a list of cities and nested dict of attributed keyed by Zipcode"""
        self.zipCodes = zipCodes
        urlList = self.updateZipCodes(zipCodes)
        weatherDict = self.getWeatherInfo(urlList)
        self.cityList, self.weatherInfoDict = self.formatWeatherInfo(weatherDict)
        print(self.cityList, self.weatherInfoDict)

    def updateZipCodes(self,zip_codes): #use path sys package?
        """Given list of zip codes, returns url with mapped route to city"""
        updateUrl = []
        for zipCode in zip_codes:
            url = r"http://api.openweathermap.org/data/2.5/weather?zip={},us".format(zipCode)
            url += API_KEY #concats string
            updateUrl.append(url)

        return updateUrl

    def getWeather(self, url:str):
        """Given url requests and returns api"""
        page = requests.get(url)
        return page.json()

    def threadOne(self, func,arg):
        """Given function, starts process"""
        # start = time.time()
        t = threading.Thread(target=func, args=(arg,))
        t.start()
        # t.join()
        # end = time.time()
        # diff = end - start
        return None

    def joinThreads(self, allThreads:list):
        """Give list of threads, joins the them together to end processes"""
        for thread in allThreads:
            # if thread.alive() == True:
            thread.join()
        return None

    def getWeatherInfo(self, urlList):
        """ """
        weatherDicts = []
        for url in urlList:
            cityWeatherDict = self.getWeather(url)
            weatherDicts.append(cityWeatherDict)

        return weatherDicts

    def formatWeatherInfo(self, cityData:dict):
        """Given dictionary, extracts a city list and assigns a zipcode as a key to a dictionary of city description and temp """
        ##TEMP IS NOT CORRECT NUMBER

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
            cityDict[self.zipCodes[index]] = D
            index += 1

        return cityList, cityDict




if __name__ =='__main__':
    w = Weather(ZIP_CODES)


#download indented Json
#get city
#key can be zip code
#write timing decorator

# FUNCT that returns tuple of cityList, dict zip(k), val = 'name', 'temp', 'description'

#{ '94086': 'temp':59, 'description':"SMOKEY AF"}}

#more than one city in zip