'''18. Replace the first, last, or all occurrences of a character.'''
s = input("Enter String: ")
char = input("Enter character: ")
replacechar = input("Enter character: ")
result =""
if char in s:
    for i in range(0,len(s)):
        if char == s[i]:
           m = replacechar
           result+=m+""
        else:
            result+=s[i]+""
    print(f"After removing occurence of a character {char} in a string : {result}")
          
        
else:
    print("Character not found")