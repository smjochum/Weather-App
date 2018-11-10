import requests
import threading

ZIP_CODES = [94086, 92093, 90013, 95192, 94132, 94720, 95064, 95819, 92697, 93940, 94544]

SAMPLE_URL = r"https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22" #MTV

API_KEY = "&APPID=3a4d4260edbb76d3c27c71f306b44c9c"

class Weather:
    #__slots__ = ['zipCodes', 'cityList', 'weatherInfoDict']
    def __init__(self, zipCodes:list):
        """Given a list of zipCodes parces weather API into a list of cities and nested dict of attributed keyed by Zipcode"""
        self.zipCodes = zipCodes
        urlList = self.updateZipCodes(zipCodes)
        weatherListOfDicts = self.getWeatherInfo(urlList)
        self.cityList, self.weatherInfoDict = self.formatWeatherInfo(weatherListOfDicts)
        print(self.cityList, self.weatherInfoDict) # THESE ARE THE THINGS YOU NEED        :-)  ***HUE***

    def updateZipCodes(self,zip_codes): #use path sys package?
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
        # import pdb; pdb.set_trace()
        page = requests.get(url)
        result_data.append(page.json()) #page.json()


    def getWeatherInfo(self, urlList):
            """ Given urls with appropriate routes, """
            listOfThreads = []
            resultData = []
            for url in urlList:
                t = threading.Thread(target=self.getWeather, args=(url, resultData))
                t.start()
                listOfThreads.append(t)

            self.joinThreads(listOfThreads)
            return resultData

    def joinThreads(self, allThreads:list):
        """Give list of threads, joins the them together to end processes"""
        for thread in allThreads:
            # if thread.alive() == True:
            thread.join()
        return None



    def formatWeatherInfo(self, cityData:dict):
        """Given dictionary, extracts a city list and assigns a zipcode as a key to a dictionary of city description and temp """

        '''  
            Added: function to change from KelvinToFahrenheit

        '''

        ##TEMP IS NOT CORRECT NUMBER

        cityList = []
        index = 0
        cityDict = {}

        type(cityData)

        for city in cityData:
            cityName = city.get("name")
            cityList.append(cityName)
            D = {}
            L = city.get("main")
            
            # Add changing from Kelvin to Fahrenheit
            D['temp'] = L.get('temp')

            
            L = city.get("weather")
            weatherDict = L[0]
            D['description'] = weatherDict.get('description')

            cityDict[cityName] = D

            index += 1

        return cityList, cityDict




if __name__ =='__main__':
    w = Weather(ZIP_CODES)


