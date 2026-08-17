'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during transmission. The encryption rule is to reverse every word individually while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop

'''
n = input("Enter Message:")
words = (n.split())
print(words)

for i in range(0,len(words)):
    w = words[i]
    
    result = ""
    for j in range(len(w)-1,-1,-1):
        result+=w[j]
    print(result,end=" ")


