'''8. Toggle the case of each character in a string.'''
n = input("Enter String: ")
result =""
for i in n:
    if 'A'<=i<='Z':
        m = chr(ord(i)+32)
        result+=m
    if 'a'<=i<='z':
        m = chr(ord(i)-32)
        result+=m
    else:
        result+=i
print(result)