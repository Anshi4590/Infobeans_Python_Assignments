'''66 Count number of sentences in a paragraph.
 P = "This. Is. Test." 
 3'''

s = input("Enter String : ")

count = 0

for i in s:
    if i == ".":
        count+=1
if count!=0:
   print(f"Total Sentences in the paragraph : {count}")

else:
    print("The Sentence is not completed......")