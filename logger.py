from time import sleep
import defs
import requests
import gather
import movement
import cooldown
import threading
import bank

def log(char):
	res = movement.movement(char, 1,7)
	cooldown.parse_and_sleep(res)
	while(True):
		res = gather.gather(char)
		if (res.status_code == 497):
			bank.move_and_deposit("iron_ore", 75, char)
			res = movement.movement(char, 1,7)
			cooldown.parse_and_sleep(res)
		else:
			cooldown.parse_and_sleep(res)

for x in [0,1,2,3,4]:
	thread = threading.Thread(target=log, args=(x,))
	thread.start()