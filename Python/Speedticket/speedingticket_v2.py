#speedingticket.py
#Trying to make a efficient and small script that can be used to track illegial drivers.
#Jason Singh, 21 February

#Modules
import time

#Variables
fine = 0
wanted_first = ["James", "Helga", "Zachary"]
wanted_last = ["Wilson" , "Norman", "Conroy "]
#Lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10, 11, 12, 13, 14]
c = [15, 16, 17, 18, 19]
d = [20, 21, 22, 23, 24]
e = [25, 26, 27, 28, 29]
f = [30, 31, 32, 33, 34]
g = [35, 36, 37, 38, 39]
h = [40, 41, 42, 43, 44]
i = [45]
finelist = []

#Functions
def addtolist(CarSpeed, SpeedLimit, fine):
    CarOverLimit = CarSpeed - SpeedLimit
    if CarOverLimit in a:
        fine = 30
        finelist.append(fine)
        print("$30 FINE")
    elif CarOverLimit in b:
        fine = 80
        finelist.append(fine)
        print("$80 FINE")
    elif CarOverLimit in c:
        fine = 120
        finelist.append(fine)
        print("$120 FINE")
    elif CarOverLimit in d:
        fine = 170
        finelist.append(fine)
        print("$170 FINE")
    elif CarOverLimit in e:
        fine = 230
        finelist.append(fine)
        print("$230 FINE")
    elif CarOverLimit in f:
        fine = 300
        finelist.append(fine)
        print("$300 FINE")
    elif CarOverLimit in g:
        fine = 400
        finelist.append(fine)
        print("$400 FINE")
    elif CarOverLimit in h:
        fine = 510
        finelist.append(fine)
        print("$510 FINE")
    elif CarOverLimit >= 45:
        fine = 630
        finelist.append(fine)
        print("$630 FINE")
    else:
        print("NO FINE")

def wanted(First_Name, Last_Name):
    if First_Name in wanted_first and Last_Name in wanted_last:
        print("========================================")
        print("WARNING! WARNING! WARNING!")
        print("{} {} HAS A ARREST WARRANT".format(First_Name, Last_Name))
        print("========================================")
    else:
        print("{} {} IS CLEAR\n".format(First_Name, Last_Name))

def menu():
    print("______________________\n")
    print("SPEED FINE CALCULATOR")
    print("______________________\n")
    print("1 | CALCULATE FINES")
    print("2 | TOTAL FINES")
    print("3 | EXIT\n")
    x = input("ENTER 1 | 2 | 3\n")
    return x

#Main routine that runs in loop
while True:
    task = menu()
    if task == "1":
            First_Name = input("DRIVER'S FIRST NAME: \n").upper()
            Last_Name =  input("DRIVER'S LAST NAME: \n").upper()
            SpeedLimit = int(input("ROAD SPEED LIMIT: \n"))
            CarSpeed = int(input("DRIVER'S SPEED: \n"))
            addtolist(CarSpeed, SpeedLimit, fine)
            wanted(First_Name, Last_Name)
    elif task == "2":
            if sum(finelist) == 0:
                print("NO RECORDS")
            else:
                print("TOTAL FINE: {}".format(sum(finelist)))
                time.sleep(1)
                print("TOTAL AMOUNT OF FINES: {}".format(len(finelist)))
    elif task == "3":
        exit()
    else:
        print("INPUT VALUE NOT ALLOWED")
