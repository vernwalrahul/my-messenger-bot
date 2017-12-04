import urllib
import json
import pprint
from googleapiclient.discovery import build

my_cse_id="006302419111304791343:vbl2wy1dhzm"
def search(query,**kwargs):
	query=str(query)
	service=build("customsearch","v1",developerKey="AIzaSyCPoiRZc4BhBU4Sp5WqZv5M1WjffEA-Vss")
	res=service.cse().list(q=query,cx=my_cse_id,**kwargs).execute();
	pprint.pprint(res)
	return res

