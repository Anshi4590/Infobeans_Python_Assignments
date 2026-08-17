'''=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5ma

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''

from collections import namedtuple

Orders = namedtuple("Orders",["id", "name", "product_name", "amount"])

n = int(input("Enter Total number of Orders : "))

list = []

for i in range(n):

    print(f"Enter Orders {i+1} Details : ")
    id   =  int(input("Enter id      : "))
    name = input("Enter  Name      : ")
    product_name = input("Enter  product_name      : ")
    amount = int(input("Enter  amount      : "))
    print()

    list.append(Orders(id,name,product_name,amount))

print(list)
count = 1
 
for i in list:
  
    print(f"Orders {count} Details : ")
    print(f"id              : {id}")
    print(f"Name            : {name}")
    print(f"product_name    : {product_name}")
    print(f"amount          : {amount}")
    count+=1

max = list[0]
sum = 0

for i in list:
    sum+=i.amount
    if i.amount>max.amount:
        max = i

print("----- Highest Value Order -----")
print(f"id              : {max.id}")
print(f"Name            : {max.name}")
print(f"product_name    : {max.product_name}")
print(f"Marks           : {max.amount}")

print()
print("TOTAL SALES : ")
print(sum)
scount = 0 # student count

for i in list :
    if i.amount>10000:
       scount+=1

print(f"The  Total number of orders above 10000  : {scount}")

