import defs
import requests
import movement
import cooldown

def move_and_deposit(item, quantity, char):
	res = movement.movement(char, 4, 1)
	cooldown.parse_and_sleep(res)
	res = deposit(item, quantity, char)
	cooldown.parse_and_sleep(res)

def deposit(item, quantity, char):
	url = defs.SERVER + '/my/' + defs.CHARS[char] +'/action/bank/deposit'
	
	data = {
		"code": item,
		"quantity": quantity
	}
	
	try:
		response = requests.post(url, headers=defs.HEADERS, json=data)
		return response
	except Exception as error:
		print(error)

	return {'status_code': -1}


# move_and_deposit("ash_wood", 99, 3)
