import defs
import requests
import movement
import cooldown

def craft(item, quantity, char):
	url = defs.SERVER + '/my/' + defs.CHARS[char] +'/action/crafting'
	
	data = {
		"code": item,
		"quantity": quantity
	}
	
	try:
		response = requests.post(url, headers=defs.HEADERS, json=data)
		print(response.json())
		return response
	except Exception as error:
		print(error)

	return {'status_code': -1}

def items():
	url = defs.SERVER + '/items/'
	
	try:
		response = requests.post(url, headers=defs.HEADERS)
		print(response.json())
		return response
	except Exception as error:
		print(error)

	return {'status_code': -1}

# craft("stick", 1, 0)
items()