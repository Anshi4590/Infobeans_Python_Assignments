'''
A
BB
CCC
DDDD
EEEEE
'''
n = int(input("Enter number :"))
i =1
x = 65
while i<=n:
      print()
      j = 1
      while j<=i:
            print(chr(x),end="")
            j+=1
      x+=1
      i+=1