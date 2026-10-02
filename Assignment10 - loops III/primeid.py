'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3'''

n=int(input("enter the number="))
num=n+1
i=2
while True:
       
       i=2
       while num>i:
          if num%i==0:
               num=num+1
               break
          i=i+1   
       else:
            break
       
print(num)
print(num-n)