'''13. Get the Unicode code point before a given index.'''
n = input("Enter String:")
index = int(input("Enter index:"))
m = ord(n[index-1])
print(f"The unicode of the character at an index {index} is {m}")
