'''8. Smart Farming Irrigation System

A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

Input:
Soil Moisture = 25
Temperature = 36
Crop = wheat

Output:
Irrigation = High Water Supply'''


moisture = int(input("Soil Moisture ="))
temp = int(input("Temperature ="))
crop = input("Crop =")
rain = input("Rainfall Prediction =")

if moisture<=30:
   if temp>=35:
      if crop.lower() == "wheat":
         print("High water supply")
      else:
         print("Moderate supply")
   else:
      print("Moderate Supply")

else:
   if moisture<=60:
      if rain.lower() == "yes":
         print("Delay irrigation ")
      else:
         print("light irrigation ")
   else:
      print("No Irrigation")
