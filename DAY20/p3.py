'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:

```
e
```

'''

s = input("Enter string:")
for i in range(0,len(s)):
    count =0
    for j in range(0,len(s)):
        if s[i] == s[j]:
           count+=1
    if count==1:
       print(s[i])
       break

#using count method
s = input("Enter string:")

for i in s:
	m = s.count(i) 
	if m==1:
	   print(i)
       #break
   
