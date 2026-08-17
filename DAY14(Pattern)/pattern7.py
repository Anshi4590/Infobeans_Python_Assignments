
'''    
    1
   10
  101
 1010
10101'''







n = int(input("Enter number"))
i = 1
while i <=n:
      print()
      j=n-i
      while j>=1:
         print(" " ,end = "")
         j = j-1
      y = 1 
      while y<=i:
            if y%2==0:
               print(0,end ="")
            else:
               print(1,end ="")
            y=y+1 
      i =i+1
