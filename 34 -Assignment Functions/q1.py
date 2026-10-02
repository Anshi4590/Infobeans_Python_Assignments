'''1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

        Accept the following information from the user:

        Patient ID
        Patient Name
        Age
        Gender
        Disease
        Doctor Name

        Store the record in the nested dictionary.

        Validation:
        If the Patient ID already exists, display:

        Patient ID already exists.

2. Search Patient

        Accept Patient ID from the user.

        If the patient exists, display complete information.

        Sample Output

        Patient ID : 101
        Name       : Ajay
        Age        : 35
        Gender     : Male
        Disease    : Fever
        Doctor     : Dr. Sharma

        If Patient ID is not found:

        Patient Record Not Found

3. Update Patient Disease

        Accept Patient ID.

        If found:

        Ask for new disease.
        Update the disease information.

        Sample Output

        Disease Updated Successfully

4. Delete Patient Record

        Accept Patient ID.

        If found:

        Remove the patient record.

        Sample Output

        Patient Record Deleted Successfully

        Otherwise:

        Patient Not Found

5. Display All Patients

        Display all patient records in a formatted manner.

        Sample Output :

        --------------------------------
        Patient ID : 101
        Name       : Ajay
        Age        : 35
        Disease    : Fever
        Doctor     : Dr. Sharma
        --------------------------------

        Patient ID : 102
        Name       : Ravi
        Age        : 42
        Disease    : Diabetes
        Doctor     : Dr. Gupta

6. Count Total Patients

        Display the total number of patients currently stored.

        Sample Output

        Total Patients : 25

7. Display Patients By Disease

        Accept a disease name from the user.

        Display all patients suffering from that disease.

        Sample Output

        Enter Disease : Fever

        101  Ajay
        108  Aman
        115  Neha

        If no patient is found:

        No Patient Found

8. Display Oldest Patient

        Find and display the patient having the highest age.

        Sample Output

        Oldest Patient Details

        Patient ID : 110
        Name       : Ravi
        Age        : 68
        Disease    : Diabetes
        Doctor     : Dr. Gupta


9. Display Youngest Patient

        Find and display the patient having the minimum age.

        Sample Output

        Youngest Patient Details

        Patient ID : 121
        Name       : Riya
        Age        : 4
        Disease    : Viral Fever
        Doctor     : Dr. Mehta
        10. Exit

        Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System'''

d ={}

def add():

    name = input("Enter Name : ")
    gender = input("Enter Gender : ")
    age = int(input("Enter Age : "))
    disease = input("Enter Disease : ")
    doctor = input("Enter Doctor : ")
    d[id] ={"Name":name , "Age":age,"Gender" : gender ,"Disease":disease ,"Doctor" : doctor}
    print("Patient added Sucessfully.....")

def search():
    print(d[id])

def update():

    newdisease = input("Enter Disease : ")
    d[id]["Disease"] = newdisease
    print(" Disease Updated Successfully......")


def delete():

    del d[id]
    print("Patient Record Deleted Successfully.....")

def display():

    for i in d:

        print()
        print("---------------")
        print(f"Patient_Id : {id}")
        print(f"Name       : {[id]["Name"]}")
        print(f"Gender     : {[id]["Gender"]}")
        print(f"Age        : {[id]["Age"]}")
        print(f"Disease    : {[id]["Disease"]}")
        print(f"Doctor     : {[id][""]}")
        print("---------------")

def count():

   count = len(d) 
   print(f"Total count : {count}")


def disease():

    disease = input("Enter disease :")

    for i in d:

       if d[i]["Disease"] == disease:
           print(f"{i}  :  {d[i]["Name"]}")

def oldest():

    max = 0

    for i in d:

        if d[i]["Age"]>max:
            max = d[i]["Age"]
            id = i

    print("Oldest Patient Details")
    print(f"Patient_Id : {id}")
    print(f"Name       : {[id]["Name"]}")
    print(f"Gender     : {[id]["Gender"]}")
    print(f"Age        : {[id]["Age"]}")
    print(f"Disease    : {[id]["Disease"]}")
    print(f"Doctor     : {[id][""]}")

def youngest():

    young = d[0]["Age"]
    id = 0

    for i in d:

        if d[i]["Age"] < young:
            young = d[i]["Age"]
            id = i

    print("Oldest Patient Details")
    print(f"Patient_Id : {id}")
    print(f"Name       : {[id]["Name"]}")
    print(f"Gender     : {[id]["Gender"]}")
    print(f"Age        : {[id]["Age"]}")
    print(f"Disease    : {[id]["Disease"]}")
    print(f"Doctor     : {[id][""]}")


while True :

    print("""=====================================
              HOSPITAL PATIENT MANAGEMENT SYSTEM
            =====================================

            1. Add New Patient
            2. Search Patient
            3. Update Patient Disease
            4. Delete Patient Record
            5. Display All Patients
            6. Count Total Patients
            7. Display Patients By Disease
            8. Display Oldest Patient
            9. Display Youngest Patient
            10. Exit""")

    choice = int(input("Enter choice : "))

    match choice:

        case 1:

            print("Add New Patient ")
            id = int(input("Enter Patient Id : "))

            if id not in d :
                add()

            else:
                print("Patient ID already exists.")


        case 2:

            print("Search Patient")
            id = int(input("Enter Patient Id : "))

            if id in d :
               search()
            
            else:
                print("Patient Record Not Found")


        case 3:

            print("Update Patient details")
            id = int(input("Enter Patient Id : "))

            if id in d :
                update()
            
            else:
                print("Patient Record Not Found")


        case 4:

            print(" Delete Patient ")
            id = int(input("Enter Patient Id : "))

            if id in d :
               delete()
            
            else:
                print("Patient Record Not Found")

        case 5:

            print(" Display Patient ")
            display()

        case 6:

            print("Count Total Patient ")
            count()

        case 7:
             disease()
            
        case 8:

            oldest()

        case 9:

            youngest()

        case 10:
            print("Exiting the menu.....")
            break
         




