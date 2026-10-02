'''
*
 *
  *
   *
    *
'''



n = int(input("Enter number:"))
i=1
while i<=n:
     print()
     j = 1
     while j<=i:
          if i==j:
             print("*")
          else:
             print(" ",end ="")
          j+=1
     i+=1
