'''2. An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800'''

#solution:

value = int(input("Cart value:"))
type  = input("User Type (premium/regular) :")

if value>=5000:

    if type.lower()== "premium":
       value = value - value*20/200
       print("Final Amount:",value)

    else:
       value = value - value*10/100
       print("Amount:",value)

else:

    if value>=2000:
        value = value - value*5/100
        print("Final Amount:",value)

    else:
        print("No Discount is applied:")



