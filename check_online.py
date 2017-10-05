#To get a list of all online users.
import requests,traceback,json
param = {}
param['q'] = "SELECT uid, name, pic_square, online_presence FROM user WHERE online_presence IN ('active', 'idle') AND uid IN (SELECT uid2 FROM friend WHERE uid1 = me())"
param['access_token'] = 'EAAKkdOyVdMIBAMitYxUd3dmoRg1dBa8C8PeZAoKmU7rM6Hh2GiXFrEzpOeMRKJZCQddt3KoaXMQVdyAbcZAcPVwloNlw9mHEshFAsQBLQOl4sciruwDJh6MgW1ZBGLTDbZALmk42BO5fsWCsOnynG71Kgftv4j8MD48nRpzhEwAZDZD'
param['method'] = 'GET'
try:
  response = requests.get("https://graph.facebook.com/fql%22,params=param")
except:
   print traceback.print_exc()
if response.status_code==200:
    for eachItem in json.loads(response.text)['data']:
        print eachItem['name'],'  is  ',eachItem['online_presence']
else:
    print traceback.print_exc()