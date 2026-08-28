'''9.

=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker

---'''

m = int(input("Enter total of no. students : "))

stocks = {}
ans = {}

for i in range(m):

    key = input("Enter key : ")
    value = input("Enter value : ")
    stocks[key] = value

for k ,v in stocks.items():
    
    if v<30:
       ans[i]=v

for i in ans:
    print(i)