'''
A
BCD
EFGHI
JKLMNOP

'''


n = int(input("Enter number"))

i=1
k=1
var = 65
while i<=n:
      print()
      j=1
      while j<=k:
          print(chr(var),end="")
          j+=1
          var+=1
      k=k+2
      i+=1