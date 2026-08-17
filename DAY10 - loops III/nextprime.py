'''2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17'''

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
            
      
   
   
