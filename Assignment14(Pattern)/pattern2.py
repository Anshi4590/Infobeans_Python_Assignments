
'''
A
AB
ABC
ABCD
ABCDE'''


n = int(input("Enter the number"))
i = 1
while i<=n:
      print()
      j =1
      x=65
      while j<=i:
         print(chr(x),end ="")
         x = x+1
         j =j+1
      i = i+1  
    