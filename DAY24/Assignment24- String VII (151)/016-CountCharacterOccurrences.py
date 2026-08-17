'''16. Count total occurrences of a character in a string.'''
s = input("Enter String: ")
char = input("Enter character: ")
count = 0
if char in s:
    for i in range(0,len(s)):
        if char == s[i]:
           count+=1
    print(f"The total occurence of a character {char} in a string : {count}")
          
        
else:
    print("Character not found")