'''
    X 
   X X 
  X___X
 X_____X
X X X X X

'''

n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
     for j in range (0,n-i):
         print(" ",end="")
     
     for k in range (1,i+1):
         if k==1 or k==i :
            print("x",end="")

         elif i==n:
            print("x",end=" ")
         else:
            print("__",end="")
         
         
     print()
