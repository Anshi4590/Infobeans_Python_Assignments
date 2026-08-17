'''6.

Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.


Input:

24


Output:

Next Prime Cabin = 29'''


n = int(input("enter the number"))

m = n+1

ans=0

flag = True # here false means my num is prime

for i in range(m,n*2):
   for i in range(2,m//2+1):
        if m%i == 0:
           flag =False
           break
   if flag:
      ans=m
      break 
   else:
      m+=1
      flag=True

print(ans)