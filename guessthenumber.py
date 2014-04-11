#guessthenumber.py

import random
counter = 0
number = random.randint(1, 100)
while True:
	guess = input("Tebakan anda: ")
	counter = counter + 1
	if guess == number:
		print 'Anda menang. Jumlah tebakan: ', counter
		break
	elif guess > number:
		print 'Terlalu besar'
	else:
		print 'Terlalu kecil'


