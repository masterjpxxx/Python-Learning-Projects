#This python program can perform an action after a desired time has been passed to the timer function
#Step 1: Import time library
#Step 2: Ask the user for the countdown time in seconds
#Step 3: Display a message at the end of the timer

import time


def countdown(t):
    while(t):
        min, secs = divmod(t, 60)
        timer = '{:02d}:{02d}'.format(min, secs)
        print(timer, end='\r')
        time.sleep(1)
        t-=1
    print("Timer completed!")
    
    
time = int(input("Please input time in seconds: "))
countdown(time)