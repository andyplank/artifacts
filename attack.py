import defs
import requests

def attack():
	url = defs.SERVER + '/my/' + defs.CHARS[0] +'/action/fight'
	
	try:
		response = requests.post(url, headers=defs.HEADERS)
		data = response.json()
		print(data)
	except Exception as error:
		print(error)
