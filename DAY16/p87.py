'''

*         *
**       **
***     ***
****   ****
***** *****

'''
n = int(input("Enter number:"))
i = 1
while i<=n:
      print()
      j = 1
      while j<=i:
          print("*",end="")
          j+=1
      k=1
      while k<=2*(n-i)+1:
          print(" ",end="")
          k+=1
      m = 1
      while m<=i:
          print("*",end="")
          m+=1
      i+=1
      