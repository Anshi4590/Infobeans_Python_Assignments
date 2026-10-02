'''=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''

from collections import namedtuple

book = namedtuple("book",["id", "title", "author", "price"])

n = int(input("Enter Total number of books : "))

list = []

for i in range(n):

    print(f"Enter Books {i+1} Details : ")
    id   =  int(input("Enter id      : "))
    title = input("Enter  title     : ")
    author = input("Enter  author     : ")
    price = int(input("Enter  price      : "))
    print()

    list.append(book(id,title,author,price ))

print(list)
count = 1
 
for i in list:
  
    print(f"Orders {count} Details : ")
    print(f"id              : {i.id}")
    print(f"title           : {i.title}")
    print(f"author          : {i.author}")
    print(f"price           : {i.price }")
    count+=1

max = list[0]
sum = 0

for i in list:
    sum+=i.price
    if i.price>max.price:
        max = i

avg= sum /n

print("----- Highest Value book -----")
print(f"id              : {max.id}")
print(f"title           : {max.title}")
print(f"author          : {max.author}")
print(f"price           : {max.price }")

print()
print(f"The Average Marks   : {avg}")
author = input("Enter author name : ")
scount = 0 # student count

for i in list :
    if i.author==author:
       print(i.id,i.title,i.author,i.price)


