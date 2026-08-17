'''
1
22
3 3
4  4
55555

'''
n = int(input("Enter number : "))
i =1
while i<=n:
      print()
      j =1
      while j<=i:
           if i==j or j ==1 or i==n:
              print(i,end="")
           else:
              print(" ",end ="")
           j+=1
      i+=1
