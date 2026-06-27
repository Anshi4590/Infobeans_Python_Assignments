'''8. E-Commerce Dynamic Pricing System

An e-commerce system gives discount based on demand, stock, user type, and festival.

If demand is 80 or above, then check stock. If stock is less than 50, then check user type. If user is premium, then check festival. If festival is yes, give 20% discount; otherwise 10%. If user is not premium, no discount. If stock is 50 or more, give 5% discount.

If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.

If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

Input:
Demand = 85
Stock = 40
User Type = premium
Festival = yes

Output:
Discount = 20%'''

#solution
Demand = int(input("Demand = "))
Stock = int(input("Stock = "))
Type = input("User Type = ")
Festival = input("Festival = ")

if Demand>=80:

   if Stock<50:

      if Type.lower() == "premium":

         if Festival.lower() =="yes":
            print("Discount = 20%")

         else:
            print("Discount = 10%")

      else:
         print(" No Discount")

   else:
      print("Discount = 5%")

elif 40<=Demand<=79:

    if Festival.lower() == "yes":
       print("Discount = 10%")

    else:
       print(" No Discount ")

else:

    if Stock>200:
       print("Discount = 15%")

    else:
       print(" No Discount")
