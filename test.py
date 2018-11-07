import requests
import threading
import time


ZIP_CODES = [92093, 90013, 95192, 94132, 94720, 95064, 95819, 92697, 93940, 94544]

SAMPLE_URL = r"https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22" #MTV

API_KEY = "&APPID=3a4d4260edbb76d3c27c71f306b44c9c"


def updateZipCodes():
    updateUrl = []
    for zip in ZIP_CODES:
        url = r"http://api.openweathermap.org/data/2.5/weather?zip={},us".format(zip)
        url += API_KEY #concats string
        updateUrl.append(url)
    return updateUrl

def getWeather(url:str):
    page = requests.get(url)
    return page.json()

def timeOne(func,arg):
    start = time.time()
    t = threading.Thread(target=func, args=(arg,))
    t.start()
    t.join()
    end = time.time()
    diff = end - start
    return diff

def getWeatherInfo(urlList):
    weatherDicts = []
    for url in urlList:
        cityWeatherDict = getWeather(url)
        weatherDicts.append(cityWeatherDict)
    return weatherDicts


if __name__ =='__main__':
    urlList = updateZipCodes()
    weatherDicts = getWeatherInfo(urlList)



#download indented Json
#get city 'name', 'temp', 'description'