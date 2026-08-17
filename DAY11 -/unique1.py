'''Unique Digit Security Scanner


A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept


Input:

57294


Output:

Valid Unique Code'''


n = int(input("enter number"))
count =0
i = 1
while n>0:
   d = n%10
   n = n//10
   print(d)

   while n>0:
     d1 = n%10
     if d == d1:
         count=count+1
     n=n//10

if count==0:
      print("Unique code")
else:
      print("not Unique")
    
   
   




