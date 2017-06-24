
import requests
import pyowm

def weather(city):
	city=str(city)
	site='http://api.openweathermap.org/data/2.5/weather?APPID=9ab926ca6309ff7f06ed89e19f374271&q='+str(city)
	r = requests.get(site)
	p=r.json()
	text=""
	
	text+=str("City: "+str(p['name'])+str(" Country: ")+str(p['sys']['country'])+"\n");
	text+=("Temp: "+str(float(p['main']['temp'])-273.15)+" deg C"+"\n");
	text+=("Humidity: "+str(p['main']['humidity'])+"\n");

	return (text)

