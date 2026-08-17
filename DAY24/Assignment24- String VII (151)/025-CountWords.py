'''25 Count total words in a string
 S = "This is a test" 
 output = 4'''

n = input("Enter String: ")
m = n.split()
count = 0
for i in m:
    count+=1
print(count)