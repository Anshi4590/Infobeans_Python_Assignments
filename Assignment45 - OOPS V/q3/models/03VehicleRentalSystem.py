'''
============================================================
ASSIGNMENT 3 � VEHICLE RENTAL SYSTEM
====================================


A vehicle rental company rents different types of vehicles.

Create:

Vehicle
|
+-------- Car
|
+-------- Bike

REQUIREMENTS:

1. Create Vehicle class.

Attributes:

* vehicle_number
* brand
* rent_per_day

2. Car should inherit from Vehicle.

Additional:

* number_of_seats

3. Bike should inherit from Vehicle.

Additional:

* engine_cc

4. Initialize parent data using super().

5. Create:

display_vehicle()
calculate_rent(days)

6. Override calculate_rent() in Car and Bike.

7. The child methods must call the parent calculation using super().

8. Use a property for rent_per_day.

9. Create:

@property
@rent_per_day.setter
@rent_per_day.deleter

10. rent_per_day must be greater than 0.

11. Read all information from the user.

INPUT:

Enter Vehicle Number:
Enter Brand:
Enter Rent Per Day:
Enter Vehicle Type:

1. Car
2. Bike

If Car:

Enter Number of Seats:

If Bike:

Enter Engine CC:

Enter Number of Rental Days:

SAMPLE INPUT:

Enter Vehicle Number: MP09AB1234
Enter Brand: Hyundai
Enter Rent Per Day: 1500
Enter Vehicle Type: 1
Enter Number of Seats: 5
Enter Number of Rental Days: 4

EXPECTED OUTPUT:

## Vehicle Details

Vehicle Number: MP09AB1234
Brand: Hyundai
Rent Per Day: 1500
Vehicle Type: Car
Number of Seats: 5

Rental Days: 4
Total Rent: 6000
'''
class Vehicle:

    def __init__(self, vehicle_number, brand, rent_per_day):

        # parent attributes
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.rent_per_day = rent_per_day

    @property
    def rent_per_day(self):
      
        return self.__rent_per_day

    @rent_per_day.setter
    def rent_per_day(self, value):

        if self.__rent_per_day>0:
           self.__rent_per_day = value

    @rent_per_day.deleter
    def rent_per_day(self):
        del self.__rent_per_day

    def display_vehicle(self):
        print(f"Vehicle Number   : {self.vehicle_number}")
        print(f"Brand            : {self.brand }")
        print(f"Rent             : {self.__rent_per_day}")

    def calculate_rent(self, days):
        print(f"Total Rent:   {self.__rent_per_day*days}")


class Car(Vehicle):

    def __init__(self, vehicle_number, brand, rent_per_day, number_of_seats):

        super().__init__(vehicle_number, brand, rent_per_day)
        self.number_of_seats = number_of_seats

        
    def display_vehicle(self):
        super().display_vehicle(self)
        print(f"Number of seats : {self.number_of_seats}")
       

    def calculate_rent(self, days):
        
        return self.__rent_per_day*days


class Bike(Vehicle):

    def __init__(self, vehicle_number, brand, rent_per_day, engine_cc):
        super().__init__(vehicle_number, brand, rent_per_day)
        self.engine_cc = engine_cc
        

    def display_vehicle(self):
        super().display_vehicle(self)
        print(f"Engine CC : {self.engine_cc}")

    def calculate_rent(self, days):
        return self.__rent_per_day*days
        