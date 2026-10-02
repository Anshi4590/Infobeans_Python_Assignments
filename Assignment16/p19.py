'''
*
* *
*   *
*     *
* * * * *
'''

n = int(input("Enter number:"))
i = 1
while i<=n:
      print()
      j = 1
      while j<=i:
            if j == 1 or i ==j or i==n:
               print("*",end=" ")
            else:
               print(" ",end=" ")
            j+=1
      i+=1