'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km'''


speed = int(input("enter the speed:"))
hours = int(input("enter the hour:"))
min = int(input("enter the minutes:"))

totaltime = (hours+(min/60))
distance = totaltime*speed
print("Total Time =",totaltime,"hours")
print("Distance =",distance,"km")


