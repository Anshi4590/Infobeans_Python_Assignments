'''
1
12
1 3
1  4
12345

'''
n = int(input("Enter number : "))
i =1
while i<=n:
      print()
      j =1
      while j<=i:
           if i==j or j ==1 or i==n:
              print(j,end="")
           else:
              print(" ",end ="")
           j+=1
      i+=1

