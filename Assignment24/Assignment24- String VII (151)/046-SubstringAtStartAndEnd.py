'''46 Check if a substring appears at both the start and end. 

S = "abcabca", 
Sub="abca" 
output 

TRUE'''

string = input("Enter String : ")
substring = input("Enter Substring : ")

if string[:len(substring)] == substring and string[len(string)-len(substring):len(string)] == substring:
    print("True")
else:
    print("False")