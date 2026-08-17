'''
A
AB
ABC
ABCD
ABCDE
'''
n = int(input("Enter number: "))
i = 1
while i<=n:
    print()
    j = 1
    x = 65
    while j<=i:
         print(chr(x),end="")
         x+=1
         j+=1
    i+=1

