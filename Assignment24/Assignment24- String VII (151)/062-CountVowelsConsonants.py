'''62 Count vowels and consonants. 
S = "apple" 
Vowels: 2, 
Consonants: 3
'''
s = input("Enter String : ").lower()

vcount = 0
Ccount = 0
for i in s :

    if i>="a" and i<="z":

        if i in "aeiou":
            vcount+=1

        else:
            Ccount+=1
            
print(f"vowels : {vcount} ")
print(f"Consonents : {Ccount}")
