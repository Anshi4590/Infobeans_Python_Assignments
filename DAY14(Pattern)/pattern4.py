
'''
    1
   21
  321
 4321
54321'''


n = int(input("Enter number"))
i = 1
while i <=n:
      print()
      j=n-i
      while j>=1:
         print(" " ,end = "")
         j = j-1
      y = i
      while y>=1:
         print(y,end="")
         y = y-1
      i = i+1