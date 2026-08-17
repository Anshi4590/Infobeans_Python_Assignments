'''
    A
   AB
  ABC
 ABCD
ABCDE
'''

n = int(input("Enter the value of n:"))
i = 1
while i<=n:
      print()
      j=1
      while j<=n-i:
         print(" ",end="")
         j+=1
       
      m = 65
      for k in range(0,i):
         print(chr(m),end ="")
         m+=1
      i+=1
      
