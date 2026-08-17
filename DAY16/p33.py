'''
ABCDE
ABCD
ABC
AB
A

'''

n = int(input("Enter number :"))
i = n

while i>=1:
      print()
      j = 1
      k = 65
      while j<=i:
            print(chr(k),end="")
            k+=1
            j+=1
      
      i-=1