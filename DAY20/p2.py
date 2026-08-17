'''
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:

```
Python is powerful
```

Output:

```
lufrewop si nohtyP

'''

n = input("Enter String:")
result=""
for i in range(len(n)-1,-1,-1):
    result+=n[i]
print(result)


# using split
n = input("Enter String:")
result=""

words = n.split()
print(words)
for i in range(len(words)-1,-1,-1):
    w = words[i]
    rev=""
    for j in range(len(w)-1,-1,-1):
        rev+=w[j]
    print(rev,end=" ")
    