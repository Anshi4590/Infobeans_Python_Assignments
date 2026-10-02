'''15. Find the last occurrence of a character in a string.'''
s = input("Enter String: ")
char = input("Enter character: ")
if char in s:
    for i in range(len(s)-1,-1,-1):
        if char == s[i]:
          print(f"The first occurence of a character {char} in a string : {i}")
          break
        
        
else:
    print("Character not found")
# using method

if char in s:
    m = s.rfind(char)    
    print(f"The first occurence of a character {char} in a string : {m}")
        
else:
    print("Character not found")
