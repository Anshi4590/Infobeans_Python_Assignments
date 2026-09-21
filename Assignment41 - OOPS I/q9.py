'''Assignment 9: Product Inventory Management

A shopkeeper wants to manage the stock of a product.

Create a class Product with the following attributes:

Product ID

Product name

Price

Available quantity

Create the following methods:

add_stock() – Increase the available quantity.

sell_product() – Decrease the available quantity.

calculate_stock_value() – Calculate price × available quantity.

display_product() – Display product and stock details.

Sample operations:

Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3

Expected result:

Available Quantity: 12
Total Stock Value: 540000'''

class Product:

    def __init__(self, product_id, product_name, price, available_quantity):

        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.available_quantity = available_quantity

    def add_stock(self,quantity):

      
        self.available_quantity = self.available_quantity + quantity
        return self.available_quantity

    def sell_product(self,quantity):

        self.available_quantity = self.available_quantity - quantity
        return self.available_quantity
        
    def calculate_stock_value(self):

        ans = self.price*(self.available_quantity)
        return ans
        

    def display_product(self):
        print("Product ID         :", self.product_id)
        print("Product Name       :", self.product_name)
        print("Price              :", self.price)
        print("Available Quantity :", self.available_quantity)
        print("Total Stock Value  :", self.calculate_stock_value())


# Object creation
product = Product(101, "Laptop", 45000, 10)

# # Operations
print(product.add_stock(5))
print(product.sell_product(3))
print(product.calculate_stock_value())
product.display_product()