'''5.Number Stability Analyzer


A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number


Input:

12359


Output:

Stable Number'''


b = int(input("enter the number"))
last = b %10
b = b//10

for i in range(len(str(b))):
   second = b%10
   if second>=last:
        print("unstable number")
        break
   b = b//10
   last = second
else:
   print("stable number")


