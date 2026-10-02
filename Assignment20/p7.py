'''
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you
```

Output:

```
hello how are you
'''

n = input("Enter String :")
w = n.split()
result=""
for i in range(0,len(w)):
    ch = w[i]
    if ch in result:
       continue
    else:
       result+=w[i]+" "
print(result)
    
    

