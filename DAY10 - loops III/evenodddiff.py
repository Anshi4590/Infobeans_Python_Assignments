'''Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime'''

n = int(input("enter number"))
ecount =0
ocount =0
for i in range(len(str(n))):
    d = n%10
    n=n//10
    if d%2==0:
       ecount+=1
    else:
       ocount+=1
diff = abs(ecount-ocount)
print(ecount)
print(ocount)
print(diff)
if diff<=1:
   print("not prime")
else:
   for i in range(2,diff//2+1):
      if diff%i==0:
        print("not prime")
        break
   else:
      print("prime number")

