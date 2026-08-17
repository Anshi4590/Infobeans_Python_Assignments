
'''
    *
   **
  ***
 ****
*****
'''



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
         print("*",end="")
         y = y-1
      i = i+1