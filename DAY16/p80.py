'''
1
12
123
1234
123
12
1

'''
n =int(input("Enter number:"))
i = 1
while i<=n:
      print()
      j=1
      while j<=i:
         print(j,end="")
         j+=1
      i+=1
m = n-1
k = 1
i-=1
while k<=m :
      print()
      l = 1 
      while l<=(2*n-i)-1:
         print(l,end="")
         l+=1
      i+=1
      k+=1


  