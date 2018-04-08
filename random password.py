import random

print("enter if you want a weak, avg or strong password")


passList = "QWERTYUIOPASDFGHJKLZXCVBNM"
passList2 = "qwertyuiopasdfghjklzxcvbnm"
passList3 = "1234567890!@#$%^&*()_+"

newPassword = input()

def weakpass():
        newpass = random.sample(passList , 8)
        newpass = "".join(newpass)
        print(newpass)

def avgpass():
    avglist = passList + passList2
    newpass = random.sample(avglist, 8)
    newpass = "".join(newpass)
    print(newpass)

def strongpass():
    strlist = passList + passList2 + passList3
    newpass = random.sample(strlist, 10)
    newpass = "".join(newpass)
    print(newpass)

if newPassword == "weak":
    weakpass()
elif newPassword == "avg":
    avgpass()
elif newPassword == "strong":
    strongpass()

