import time

def countdown_with_pause(n, delay):
	for i in range(n, 0, -1):
		time.sleep(delay)
		print(f"{i} 🔴")
		if i == 1:
			print("🥳BOOM🥳")

n = 0
delay = 0
while True:
	try:
			n = int(input("Enter a number: "))
			if n <= 0:
				print("Enter possitive number")
				continue
			else:
				print("Accept")
			time.sleep(0.5)
			delay = int(input("Enter a delay of timer: "))
			if n <= 0:
				print("Enter possitive number")
				continue
			else:
				print("Accept")
				break
	except ValueError:
		print("Error")
			
countdown_with_pause(n, delay)
		

