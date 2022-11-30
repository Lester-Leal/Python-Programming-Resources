# Simple Timer
# Author: Jorn Blaedel Garbosa

import time

# Initialize seconds, minutes, hours, to start from zero
sec=0
min=0
hr=0

# Loop infinitely
while True:
	# time.sleep(1) # Pause the timer for 1 second
	sec=sec+1 # Increment second
	print(str(hr)+":"+str(min)+":"+str(sec)) # Print the timer
	# Reset the second to zero if reached 60
	if sec==59:
		sec=-1
		min=min+1 # Increment minute
	# Reset the minute to zero if reacher 60
	if min==60:
		min=0
		hr=hr+1 # Increment hour