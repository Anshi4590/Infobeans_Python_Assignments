'''
70. Compare the number of times 'the' and 'is' appear. 
S = "the cat is on the mat" 
the: 2, is: 1 (theis)

'''
s = input("Enter String : ")
sub1 = "the"
sub2 = "is"

count1 = 0
count2 = 0

for i in range(0,len(s)-len(sub1)+1):

    if s[i:i+len(sub1)]== sub1:
        count1+=1

print(f"The count of {sub1} : {count1}")

for i in range(0,len(s)-len(sub2)+1):

    if s[i:i+len(sub2)]== sub2:
        count2+=1

print(f"The count of {sub2} : {count2}")


