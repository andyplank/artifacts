import requests
import defs

def movement(char, x, y):
	url = defs.SERVER + '/my/' + defs.CHARS[char] +'/action/move'
	data = {
		'x': x,
		'y': y
	}
	
	try:
		response = requests.post(url, headers=defs.HEADERS, json=data)
		return response
	except Exception as error:
		print(error)