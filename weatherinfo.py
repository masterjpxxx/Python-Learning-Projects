#This python program is used to generate weather data from a specified location by the user
#Step1: Import pprint and requests library'
#Step2: Register and generate an API key for weather generator website
#Step3: Ask the user for the location
#Step4: Generate the weather data using the API Call
#Step5: Display the result to the user

import requests
from pprint import pprint


def generateweatherdata(location):
    API_KEY = ''#Place your own API key here
    base_url ='http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY+"&q="+location
    weatherdata = requests.get(base_url).json()
    pprint(weatherdata)
    
    
location = input("Please specify a location: ")
generateweatherdata(location)