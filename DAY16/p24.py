'''
*
**
*@*
*@@*
* * * * *

'''
n = int(input("Enter number : "))
i =1
while i<=n:
      print()
      j =1
      k = 65
      while j<=i:
           if i==j or j ==1 :
              print("*",end="")
           elif i==n:
              print("*",end="")
           else:
              print("@",end ="")
           j+=1
           k+=1
      i+=1
