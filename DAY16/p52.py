'''
    A
   AB
  A_C
 A__D
ABCDE
'''
n = int(input("Enter number:"))
for i in range(1,n+1):
     for j in range (0,n-i):
         print(" ",end="")
     m = 65
     for k in range (1,i+1):
         if k==1 or k==i or i==n:
            print(chr(m),end="")
            
         else:
            print("_",end="")
         m+=1
     print()