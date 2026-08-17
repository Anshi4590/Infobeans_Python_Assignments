'''7. Convert a string to lowercase'''
n = input("Enter String: ")
result =""
for i in n:
    if 'A'<=i<='Z':
        m = chr(ord(i)+32)
        result+=m
    else:
        result+=i
print(result)