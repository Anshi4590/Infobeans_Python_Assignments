'''

***** *****
****   ****
***     ***
**       **
*         *

'''

n = int(input("Enter number:"))
a = n
i = 1
while i<=n:
      print()
      j = 1
      while j<=a:
          print("*",end="")
          j+=1
     
      k=1
      while k<=2*i-1:
          print(" ",end="")
          k+=1
      m = 1
      while m<=a:
          print("*",end="")
          m+=1
      a-=1
      i+=1