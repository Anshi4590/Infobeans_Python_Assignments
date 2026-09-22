'''Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations

Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150

Sample Input

Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350

Sample Output

------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0

'''

class Customer:

    def __init__(self, customer_id, customer_name, units_consumed):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.units_consumed = units_consumed

    def calculate_bill(self):
        return (self.units_consumed * 8) + 150

    def display_bill(self):
        print("\n------ Electricity Bill ------")
        print(f"Customer ID       : {self.customer_id}")
        print(f"Customer Name     : {self.customer_name}")
        print(f"Units Consumed    : {self.units_consumed}")
        print(f"Total Bill Amount : ₹{self.calculate_bill()}")


customer_id = input("Enter Customer ID : ")
customer_name = input("Enter Customer Name : ")
units_consumed = int(input("Enter Units Consumed : "))

customer = Customer(customer_id, customer_name, units_consumed)

customer.display_bill()