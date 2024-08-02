from time import sleep
import re

def parse_cooldown(response):
	data = response.json()
	if (response.status_code == 200):
		if 'data' in data and 'cooldown' in data['data']:
			cooldown_time = data['data']['cooldown']['remaining_seconds']
			print(f"Cooldown time: {cooldown_time}")
			return int(cooldown_time)
		else:
			print("Error: Cooldown field does not exist in the response data.")
	if (response.status_code == 499):
		error = data.get('error')
		if error is not None:
			message = error.get('message')
			if message is not None:
				digits = re.findall(r'\d+', message)
				if digits:
					first_digits = int(digits)
					print(f"Cooldown remaining: {first_digits}")

def parse_and_sleep(response):
	data = response.json()
	if (response.status_code == 200):
		if 'data' in data and 'cooldown' in data['data']:
			cooldown_time = data['data']['cooldown']['remaining_seconds']
			sleep(cooldown_time)
		else:
			raise ValueError("Error: Cooldown field does not exist in the response data.")
	if (response.status_code == 499):
		error = data.get('error')
		if error is not None:
			message = error.get('message')
			if message is not None:
				digits = re.findall(r'\d+', message)
				if digits:
					remaining_time = int(digits[0])
					sleep(remaining_time)