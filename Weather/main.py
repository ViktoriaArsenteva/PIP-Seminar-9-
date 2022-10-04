import tkinter
from pyowm import OWM
from tkinter import *


owm = OWM('ac1ab0051a745bdc32453b8a99d898fb')
place = input('Введите город ')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')
t1 = temp['temp']
t2 = temp['feels_like']
t3 = temp['temp_max']
t4 = temp['temp_min']


print("В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
	"Максимальная температура " + str(t3) + " °C" +"\n" + 
	"Минимальная температура " + str(t4) + " °C" + "\n" + 
	"Ощущается как " + str(t2) + " °C" )