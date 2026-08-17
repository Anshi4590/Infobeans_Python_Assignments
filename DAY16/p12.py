'''
a
ab
abc
abcd
abcde

'''
n = int(input("Enter number:"))
i = 1
while i<=n:
      print()
      j = 1
      m = 97
      while j<=i:
            print(chr(m),end ="")
            m+=1
            j+=1
      i+=1