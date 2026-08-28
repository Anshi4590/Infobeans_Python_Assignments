'''1.

=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6

---'''

m = int(input("Enter number of values :"))

d ={}
for i in range (m):
    key = input("Enter key:")
    value = int(input("Enter value:"))
    d[key] = value

s = sum(d.values())
print(f"Total Quantity :{ s }")