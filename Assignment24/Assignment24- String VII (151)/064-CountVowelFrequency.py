'''
64 Count frequency of each vowel. 
S = "programming" 
o: 1, a: 1 (e, i, u: 0)'''

s = input("Enter String:")
vowels = ""
unique = ""

for i in s:
    if i in "aeiou":
        vowels+=i

print(vowels)

for i in vowels :
    m = s.count(i)
    print(f"{i}: {m}")