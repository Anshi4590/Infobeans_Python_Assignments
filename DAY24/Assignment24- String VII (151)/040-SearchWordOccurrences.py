'''40 Search all occurrences of a word. 
S = "a b a b", 
Word='b' 2, 6 (start indices)'''

n = input("Enter string : ")
word = input("Enter word : ")

for i in range(len(n)- len(word)+1):
    flag = 0 
    for j in range(len(word)):
        if n[i+j]!= word[j]:
             flag = 1
             break
        result = i
    if flag ==0:
       print(i,end=" ")