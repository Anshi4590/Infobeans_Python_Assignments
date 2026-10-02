'''
82. Create a string from a character array. 
Char[] = {'h', 'i'} 
output = "hi"

'''

arr = list(input("Enter Character : ").split(" "))
word = ""

for i in arr:
    word+=i

print(f"string created from the given ch : {word}")