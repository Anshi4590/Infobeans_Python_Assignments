'''
A
AB
A C
A  D
ABCDE
'''
n = int(input("Enter number : "))
i =1
while i<=n:
      print()
      j =1
      k = 65
      while j<=i:
           if i==j or j ==1 or i==n:
              print(chr(k),end="")
           else:
              print(" ",end ="")
           j+=1
           k+=1
      i+=1
