'''=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2'''


from collections import namedtuple

patient = namedtuple("patient",["id", "name", "disease", "age"])

n = int(input("Enter Total number of Patient : "))

list =[]

for i in range(n):

    print(f"Enter Patient{i+1} Details : ")
    id = int(input("Enter  ID       : "))
    name = input("Enter  Name           : ")
    disease = input("Enter  Disease      : ")
    age = int(input("Enter  Age         : "))
    print()

    list.append(patient(id,name,disease,age))

print(list)
count = 1
 
for i in list:
  
    print(f"Patient {count} Details : ")
    print(f"ID           : {i.id}")
    print(f"Name         : {i.name}")
    print(f"Disease      : {i.disease}")
    print(f"Age          : {i.age}")
    count+=1


print("----- Patient Aged Above 60 ------")
for i in list :
    if i.age>60:

        print(f"ID           : {i.id}")
        print(f"Name         : {i.name}")
        print(f"Disease      : {i.disease}")
        print(f"Age          : {i.age}")


id = int(input("Enter Patient ID:"))
print("Patient Found : ")

for i in list:
    if i.id == id:
        print(i)


disease = input("Enter Disease : ")

pcount = 0 # patient count

for i in list:
    if i.disease == disease:
       pcount+=1
print(pcount)