'''11.

=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1

---'''

sales =list(input("Enter website :").split())

d = {}

for i in sales:

    d[i] = d.get(i,0)+1

print(d)

for k,v in d.items():
    print(k,":",v)