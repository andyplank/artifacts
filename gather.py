import defs
import requests

def gather(x):
	url = defs.SERVER + '/my/' + defs.CHARS[x] +'/action/gathering'
	
	try:
		response = requests.post(url, headers=defs.HEADERS)
		print(response.json())
		return response
			
	except Exception as error:
		print(error)

	return {'status_code': -1}
