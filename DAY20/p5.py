'''
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:

```
aabbccdde
```

Output:

```
5
```
'''

n = input("Enter string:")
result = ""
count = 0
for i in n:
    
    if i in result:
       continue
    else:
       result+=i+""
       count+=1
print(result)
print(count)


#identify the single unique character which is not repeated in the whole string


uniquecount = 0
for i in range(0,len(n)):
    count=0
    for j in range(0,len(n)):
        if n[i] == n[j]:
           count+=1
    if count==1:
       uniquecount+=1
print("count unique character in the string: ",uniquecount)
        

    
