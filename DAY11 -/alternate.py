'''7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime'''

n =  int(input("Enter number"))
sum =0
i=1
while n>0:
    d = n%10
    sum = sum+d
    n =n//100
print("Alternate Sum =",sum)
if sum<=1:
   print("not prime")
else:
   for i in range(2,sum//2+1):
       if sum%i == 0:
         print("not prime")
         break
   else:
      print("prime number")


    
   
   