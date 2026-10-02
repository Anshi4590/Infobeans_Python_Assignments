'''
48. Remove all vowels.
S = "aeiou XYZ"
output
    " XYZ"

'''

s = input("Enter String : ")
vowels = "aeiou"
m = ""
for i in s:
    if i.lower() not in vowels:
        m+=i
print(m)