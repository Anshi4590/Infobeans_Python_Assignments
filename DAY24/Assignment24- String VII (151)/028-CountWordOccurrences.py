'''
28 Count occurrences of a word. S = "word word other word", Word = "word" 3
'''

n = input("Enter String:")
word = input("Enter word:")
count1=0

for i in range (len(n)-len(word)+1):
    if n[i:i+len(word)] == word:
       count1+=1
print(f"The total count of the {word} is {count1}")      


# we can also solve this without silicing

count = 0
for i in range(len(n)- len(word)+1):
    flag = 0 
    for j in range(len(word)):
        if n[i+j]!= word[j]:
             flag = 1
             break
        result = i
    if flag ==0:
       count+=1
print(f"The total count of the {word} is  {count1}")      