import os
import sys
from weather import *

greeting=(["hi","hey","hello"])
def classify(msg):
    msg=msg.lower().strip()
    
    if(msg=="help"):
       return "commonly used commands: \n1.Greeting: Hi\n\n2.google <word> (for google search).\n3.weather city_name "
    if(msg in greeting):
       return "Hello! Whats up?"
    if(msg.find("google")==0):
       return "Feature for google search will be added soon."	
    if(msg.find("weather")==0):
    	try:
    		city=msg.split()[1]
    		return weather(city)
    	except:
    		return "please enter valid city name"	   
    return "sorry! I didn't get that"

if __name__ == '__main__':
    while(1):
      msg=raw_input("Enter something: ")
      print(classify(msg))	
