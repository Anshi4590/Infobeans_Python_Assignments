'''
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa

Output:
abcda
'''


n = input("Enter String : ")
result =""

for i in range(0,len(n)-1):
    if n[i]!=n[i+1]:
       result+=n[i]
print(result,n[-1],sep="")