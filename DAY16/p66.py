'''
    1
   123
  12345
 1234567
123456789

'''

n = int(input("Enter number:"))
for i in range(1,n+1):
     for j in range (0,n-i):
         print(" ",end="")
     for k in range (1,(i*2-1)+1):
         print(k,end="")
     print()