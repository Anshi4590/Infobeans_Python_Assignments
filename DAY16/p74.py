'''
123456789
 1234567
  12345
   123
    1

'''
n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
     for j in range (1,i):
         print(" ",end="")
     for k in range (1,(m*2-1)+1,+1):
         print(k,end="")
     m-=1
     print()