
'''Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500'''


distance = int (input("enter the distance:"))
mileage = int (input("enter the mileage:"))
price = int(input ("enter the price:"))
fuelneeded =  distance//mileage
cost = fuelneeded*price
print("Price:",cost)