n = int(input("Enter the number"))
i =1
while i<=n:
      print()
      j=1
      while j<=i:
         if j%2 ==0:
            print("*",end ="")
         else:
            print(j, end ="")
         j =j+1
      i =i+1