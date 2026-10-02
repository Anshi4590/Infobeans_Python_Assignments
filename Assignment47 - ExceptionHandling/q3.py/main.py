from models.drivinglicense import Person,InvalidAgeForDrivingLicenseException, InvalidMarkForDrivingLicenseException

name = input("Enter name : ")
age = int(input("Enter Age : "))
mark = int(input("Enter Mark : "))


p1 = Person(name,age,mark)

try :

    p1.check_age()
    p1.check_mark()

except InvalidAgeForDrivingLicenseException as e:

    print("InvalidAgeForDrivingLicenseException :", e)


except InvalidMarkForDrivingLicenseException as e:

    print("InvalidAgeForDrivingLicenseException :",e)

else:

    print("Approved")