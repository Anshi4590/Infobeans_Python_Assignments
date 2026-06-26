'''11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600'''


#solution


distance = int(input("enter distance in km:"))
travel_class = int(input("Enter class:"))

if distance<=100:
   print("Sleeper: Rs100 ,AC: Rs 200")

elif 100<distance<=500:
   print("Sleeper: Rs300 ,AC: Rs 600")

else:
  print("Sleeper: Rs500 ,AC: Rs 1000")