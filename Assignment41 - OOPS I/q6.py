'''Assignment 6: Electricity Bill Calculator

An electricity board wants to calculate a customer's electricity bill based on units consumed.

Create a class ElectricityBill with the following attributes:

Consumer number

Consumer name

Units consumed

Rate per unit

Fixed charge

Create the following methods:

calculate_energy_charge() – Calculate units × rate per unit.

calculate_total_bill() – Add energy charge and fixed charge.

display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600


'''

class ElectricityBill:

    def __init__(self, consumer_number, consumer_name, units_consumed, rate_per_unit, fixed_charge):

        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units_consumed = units_consumed
        self.rate_per_unit = rate_per_unit
        self.fixed_charge = fixed_charge

    def calculate_energy_charge(self):

        ans  = self.units_consumed*self.rate_per_unit
        return ans

    def calculate_total_bill(self):

        totalbill = self.calculate_energy_charge()  + self.fixed_charge
        return totalbill
    
    def display_bill(self):

        print(f"Consumer Number      :{self.consumer_number}")
        print(f"Consumer Name        :{self.consumer_name}")
        print(f"Units Consumed       :{self.units_consumed}")
        print(f"Rate Per Unit        :{self.rate_per_unit}")
        print(f"Fixed Charge         :{self.fixed_charge}")
        print(f"Energy Charge        :{self.calculate_energy_charge()}")
        print(f"Total Bill           :{self.calculate_total_bill()}")


# Object creation

bill = ElectricityBill(501, "Amit", 250, 6, 100)

# Method calls

bill.display_bill()