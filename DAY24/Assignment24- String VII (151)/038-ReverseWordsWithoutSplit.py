'''38.Reverse words without split(). 
S = "a b c" 
"c b a"'''

s = input("Enter String : ")
result = ""
word =""

for i in range(len(s)-1,-1,-1):  
    
    if s[i]!=" ":  # so this will reverse the word until " " comes
        word = s[i]+word
    else:
        # when the space arrives this will add it into the result 
        result+=word+" "
        word =""

result+=""+word # this is adding the last word
print(result)