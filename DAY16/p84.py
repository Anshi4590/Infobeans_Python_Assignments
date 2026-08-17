'''
   *
  *_* 
 *___* 
*_____*
 *___* 
  *_*
   *
'''


n = int(input("Enter number:"))
for i in range(1,n+1):
   for j in range(0,n-i):
      print(" ",end="")
   for k in range(1,(2*i-1)+1):
      if k==1 or k==(2*i-1):
         print("*",end="")
      else:
         print("_",end="")
   print()

for i in range(1,n):

   for j in range(1,i+1):
      print(" ",end="")
   for k in range(1,2*(n-i)):
      if k==1 or k==(2*(n-i)-1):
         print("*",end="")
      else:
         print("_",end="")
   
   print()