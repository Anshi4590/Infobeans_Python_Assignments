'''Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations

Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount

Sample Input

Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000


Sample Output

------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0

'''

class Product:

    def __init__(self,Product_Id,Product_Name,Quantity,Price):

        self.Product_Id = Product_Id
        self.Product_Name = Product_Name
        self.Quantity = Quantity
        self.Price = Price

    def total_amount (self ):

        total = self.Price * self.Quantity
        return total

    def calculate_discount(self):

        if self.total_amount()>5000:

           discount = self.total_amount()*10/100
           return discount

        else:

           discount = self.total_amount()*5/100
           return discount

    def final_amount(self):

        final = self.total_amount() - self.calculate_discount()
        return final

    def display(self):

        print("------ Shopping Bill ------")
        print(f"Product ID        : {self.Product_Id}")
        print(f"Product Name      : {self.Product_Name}")
        print(f"Quantity          : {self.Quantity}")
        print(f"Price Per Item    : ₹{self.Price}")
        print(f"Total Amount      : ₹{self.total_amount()}")
        print(f"Discount          : ₹{self.calculate_discount()}")
        print(f"Final Amount      : ₹{self.final_amount()}")


Product_Id = input("Enter Product_Id :  ")
Product_Name = input("Enter Product Name : ")
Quantity = int(input("Enter Quantity : "))
Price = int(input("Enter Price : "))
print()

p1 = Product(Product_Id,Product_Name,Quantity,Price)
p1.display()
