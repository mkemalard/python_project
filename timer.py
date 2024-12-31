# COUNTDOWN PROGRAM PROGRAM

import time

unit = input("Enter time unit: (h/m/s): ")
while unit != "h" and unit != "m" and unit != "s":
    print("You enter the wrong unit!")
    unit = input("Enter time unit: (h/m/s): ")
if unit == "s":
    my_time = int(input("Enter time in seconds: "))
    for x in range(my_time, 0, -1): # for loops to count my_time to 0 backwards
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1) #print every 1 second
elif unit == "m":
    my_time = int(input("Enter time in minutes: ")) * 60
    for x in range(my_time, 0, -1): # for loops to count my_time to 0 backwards
        seconds = x % 60
        minutes = int(x / 60) % 60 
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1) #print every 1 second
elif unit == "h":
    my_time = int(input("Enter time in hours: ")) * 3600
    for x in range(my_time, 0, -1): # for loops to count my_time to 0 backwards
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) 
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1) #print every 1 second
print("TIME'S UP!!!")