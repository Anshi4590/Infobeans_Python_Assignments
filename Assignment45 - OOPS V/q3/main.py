from models.vehicle import Vehicle,Bike,Car
from rich.prompt import Prompt

vehicle_number = input("Enter Vehicle Number : ")
brand = input("Enter Brand : ")
rent_per_day = int(input("Enter Rent Per Day : "))

print("Choose Vechile Code")
print("1.Car")
print("2.Bike")

choice=Prompt.ask(
    "Enter Vechile Type",
    choices=["1","2"]
)


if choice == "1":

    number_of_seats = int(input("Enter Number of seats : "))
    days = int(input("Enter Number of Rental Days:"))
    user1 = Car(vehicle_number, brand, rent_per_day, number_of_seats)
    user1.display_vehicle()

    print()

    print(f"Rental Days : {days}")
    user1.calculate_rent(days)

else:
    engine_cc = int(input("Enter Engine CC : "))
    days = int(input("Enter Number of Rental Days:"))
    user1 = Bike(vehicle_number, brand, rent_per_day, engine_cc,days)
    user1.display_vehicle()

    print()

    print(f"Rental Days : {days}")
    user1.calculate_rent()

