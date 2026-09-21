'''
Assignment 5: Shopping Bill Calculator

A retail shop wants to calculate the total bill for a customer.

Create a class ShoppingBill with the following attributes:

Product name

Product price

Quantity

Discount percentage

GST percentage

Create the following methods:

calculate_subtotal() – Calculate price × quantity.

calculate_discount() – Calculate the discount amount.

calculate_gst() – Calculate GST on the discounted amount.

calculate_final_bill() – Calculate the final payable amount.

display_bill() – Display the complete bill details.

Formula:

Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST

'''

class ShoppingBill:

    def __init__(self,pname,pprice,quantity,dpercent,gstpercent):

        self.pname  = pname
        self.pprice = pprice
        self.quantity = quantity
        self.dpercent = dpercent
        self.gstpercent = gstpercent

    def calculate_subtotal(self):

        subtotal = self.pprice*self.quantity
        return subtotal

    def calculate_discount(self):

        discount = (self.pprice*self.dpercent/100)*self.quantity
        Discounted_Amount = self.calculate_subtotal() - discount

        return Discounted_Amount 

    def calculate_gst(self):
         
        GST = self.calculate_discount()*self.gstpercent / 100

        return  GST 

    def calculate_final_bill(self):

        Final_Bill = self.calculate_discount()+ self.calculate_gst()

        return Final_Bill

    def display_bill(self):

        print(f"Product Name        :{self.pname}")
        print(f"Product Price       :{self.pprice}")
        print(f"Quantity            :{self.quantity}")
        print(f"Discount percentage :{self.dpercent}")
        print(f"GST percentage      :{self.gstpercent}")
        print(f"Subtotal            :{self.calculate_subtotal()}")
        print(f"Discounted Amount   :{self.calculate_discount()}")
        print(f"GST                 :{self.calculate_gst()}")
        print(f"Final Bill          :{self.calculate_final_bill()}")


p1 = ShoppingBill("Book",250,10,15,20)

p1.display_bill()


        