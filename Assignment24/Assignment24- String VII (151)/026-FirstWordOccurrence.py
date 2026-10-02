'''26 Find the first occurrence of a word. 
S = "Test this test", Word = "test" 
output = 10 (index)'''

n = input("Enter String:")
word = input("Enter word:")


for i in range (len(n)-len(word)+1):
    if n[i:i+len(word)] == word:
        print(f"The first occurence of the word is {i} ")
        break


# we can also solve this without silicing
result = 0
for i in range(len(n)- len(word)+1):
    flag = 0 
    for j in range(len(word)):
        if n[i+j]!= word[j]:
             flag = 1
             break
        result = i
    if flag ==0:
        print(f"The first occurence of the word is {result}")
        break