'''8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot'''


#solution


temp = int(input("Enter the temperature in celcius:"))

if temp<0:
   print("Freezing")
elif temp>=0 and temp<=20:
   print("Cold")
elif temp>=21 and temp<=35:
   print("Warm")
else:
   print("Hot")
