'''52 Remove all special characters.
 S = "a!@b#c" 
 output:

 "abc"'''

s = input("Enter String : ")
result = ""

for i in s:

    if i.lower()>="a" and i.lower()<="z":
        result+=i

    elif i>="0" and i<="9":
        result+=i

    elif i==" " or i == "_" :
        result+=i

print(result)



# we have got a method to check alpha and numeric value together that is "is.alnum"
new =""

for i in s:
    if i.isalnum() or i in" _":
        new +=i

print(new)