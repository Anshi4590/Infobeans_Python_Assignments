'''31 Remove duplicate words. S = "the cat and the dog" "the cat and dog"
'''
n = input("Enter String:")
m = n.split(" ")
result =[]
for i in m:
    if i not in result:
        result.append(i)
      
print(" ".join(result))