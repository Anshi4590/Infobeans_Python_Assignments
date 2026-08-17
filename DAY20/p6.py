'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:

```
iphone is good and iphone battery is strong
```

Word:

```
iphone
```

Output:

```
2
''' 
s = input("Enter String : ")
word = input("Enter String : ")
count =0
for i in range(0,len(s)-len(word)):
    match = 1
    for j in range(0,len(word)):
        if s[i+j]!=word[j]:
           match =0
           break
    if match ==1:
       count+=1
print(count)
    