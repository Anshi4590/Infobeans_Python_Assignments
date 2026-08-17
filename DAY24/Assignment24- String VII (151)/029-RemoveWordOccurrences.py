'''29Remove the first, last, or all occurrences of a word. 
S = "a test b test c", 
Word = "test", 
Remove All 
output - a b c'''

s = input("Enter String : ")
word = input("Enter word : ")
result = ""
m = s.split(" ")
print(m)
for i in m:
    if i == word:
       continue
    else:
       result+=i +" "
print(result)