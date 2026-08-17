'''6. Convert a string to uppercase.'''
n = input("Enter String: ")
result =""
for i in n:
    if 'a'<=i<='z':
        m = chr(ord(i)-32)
        result+=m
    else:
        result+=i
print(result)