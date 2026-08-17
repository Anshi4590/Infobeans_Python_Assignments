'''
a
bc
d f
g  j
klmno
'''
n = int(input("Enter number : "))
i =1
k = 97
while i<=n:
      print()
      j =1
      
      while j<=i:
           if i==j or j ==1 or i==n:
              print(chr(k),end="")
           else:
              print(" ",end ="")
           j+=1
           k+=1
      i+=1
