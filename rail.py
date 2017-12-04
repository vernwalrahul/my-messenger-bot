import requests
import datetime

base_url = "http://api.railwayapi.com/v2/"

api_key = "826e521bi3"   ## Put your own key provided by railwayapi


def live_status(train_no,date):
	date_str = str(date)
	url = base_url + "live/train/" + str(train_no)+"/date/"+date_str+"/apikey/"+api_key+"/"
	response = requests.get(url) 
	p = response.json()
	status = p['response_code']
	print(date_str)
	if status == 404:
		return ("Invalid input")
	elif status == 210:
		return ("The train does not run today")
	elif status == 200:
		return p['position']



def pnr_status(pnr):
	url = base_url + "pnr-status/pnr/" + pnr+"/apikey/"+api_key+"/"
	response = requests.get(url)
	p = response.json()
	status = p['response_code']
	if status == 221:
		return("Invalid PNR")
	elif status == 220:
		return("Flushed PNR")
	elif status == 200:
		text=""
		text+=str("From Stn: ")+str(p['from_station']['code']+"\n")
		text+=str("To Stn: ")+str(p['to_station']['code']+"\n")
		text+="SN."+" "+"Booking Status"+" "+"Current Status"+"\n"
		for k in p['passengers']:
			text+=str(k['no'])+"     "+str(k['booking_status'])+"     "+str(k['current_status'])+"\n"
		return text





def train_btw_stations(src,des,date):
	url = base_url + "between/source/" + str(src)+"/dest/"+str(des)+"/date/"+str(date)+"/apikey/"+api_key+"/"
	print(url)
	response = requests.get(url)
	p = response.json()
	status = p['response_code']
	if status == 404:
		return ("Invalid input")
	elif status == 210:
		return ("The train does not run today")
	elif status == 200:
		text = ""
		text+=str("Trn no: ")+str("Trn name ")+str("SRC Dept. ")+str("DES Arr. ")+"\n"
		for k in p['trains']:
			text+=str(k['number'])+'--'+str(k['name'])+'--'+str(k['src_departure_time']+'--'+str(k['dest_arrival_time']))+"\n"
		print(text)
		return text



def train_fare(train_no,src,des,age,date,pref,quota='GN'):
	url = base_url + "fare/train/"+str(train_no)+"/source/"+str(src)+"/dest/"+str(des)+"/age/"+str(age)+"/pref/"+str(pref)+"/quota/"+str(quota)+"/date/"+str(date)+"/apikey/"+api_key+"/"
	response = requests.get(url)
	p=response.json()
	status = p['response_code']
	if status == 404:
		return("Invalid input")
	elif status == 210:
		return ("The train does not run today")
	elif status == 200:
		return p['fare']



def seat_avail(train_no,src,des,age,date,pref,quota='GN'):
	url = base_url + "check-seat/train/"+str(train_no)+"/source/"+str(src)+"/dest/"+str(des)+"/date/"+str(date)+"/pref/"+str(pref)+"/quota/"+str(quota)+"/apikey/"+api_key+"/"
	print(url)
	response = requests.get(url)
	p=response.json()
	status = p['response_code']
	if status == 404:
		return("Invalid input")
	elif status == 210:
		return("The train does not return today")
	elif status == 200:
		text = ""
		for k in p['availability']:
			text+=str(k['date'])+" --- "+str(k['status'])+"\n"
		return text










