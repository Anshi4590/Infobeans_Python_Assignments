'''12. Get the Unicode code point of a character at an index.'''
n = input("Enter String:")
index = int(input("Enter index:"))

for i in range(0,len(n)):
    if i == index:
       m = ord(n[index])
       print(f"The unicode of the character at an index {index} is {m}")
    else:
       print("Invalid syntax")
       break