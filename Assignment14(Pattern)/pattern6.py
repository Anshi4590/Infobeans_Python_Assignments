
'''
 654321
  65432
   6543
    654
     65
      6'''

n = int(input("Enter number"))
i =1
while i<=n:
      print()
      m = 1
      while m<=i:
          print(" ", end = "")
          m = m+1
      j = n
      while j>=i:
          print(j, end ="")
          j =j-1
      i =i+1