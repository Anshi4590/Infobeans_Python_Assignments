'''14. Find the first occurrence of a character in a string.'''
s = input("Enter String: ")
char = input("Enter character: ")
if char in s:
    for i in range(0,len(s)):
        if char == s[i]:
          print(f"The first occurence of a character {char} in a string : {i}")
          break
        
else:
    print("Character not found")
