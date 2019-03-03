#speedingticket.py
#Trying to make a efficient and small script that can be used to track illegial drivers.
#Jason Singh, 21 February

#Modules
import time
import re

#Variables
fine = 0
wanted_first = ["JAMES", "HELGA", "ZACHARY"]
wanted_last = ["WILSON" , "NORMAN", "CONROY"]
#Lists
finelist = []
firstlist = []
lastlist = []
speedlist = []
fines_for_each_overspeed = {"0":  0,
                            "9": 30,
                            "14": 80,
                            "19": 120,
                            "24": 170,
                            "29": 230,
                            "34": 300,
                            "39": 400,
                            "44": 510,
                            "45": 630}
def summary():
    for i in range(0, len(speedlist)):
        print("FIRST NAME: {}".format(firstlist[i]))
        print("LAST NAME: {}".format(lastlist[i]))
        print("OVERSPEEDING BY: {} km".format(speedlist[i]))
def addtolist(CarSpeed, SpeedLimit, fine):
    CarOverLimit = CarSpeed - SpeedLimit

    # Go through the l possible overspeeds until you find one that matches the car's.
    for overspeed in fines_for_each_overspeed.keys():
        if CarOverLimit <= int(overspeed):
            break
    # Then your fine is just the value associated to the overspeed key.
    fine = fines_for_each_overspeed[overspeed]

    if fine > 0:
        print("${} FINE".format(fine))
        firstlist.append(First_Name)
        lastlist.append(Last_Name)
        speedlist.append(CarOverLimit)
        finelist.append(fine)
    else:
        print("NO FINE")

def wanted(First_Name, Last_Name):
    if First_Name in wanted_first and Last_Name in wanted_last:
        print(f"""========================================
        \nWARNING! WARNING! WARNING!\n{First_Name} {Last_Name} HAS A ARREST WARRANT\n
========================================""")
    else:
        print("{} {} IS CLEAR\n".format(First_Name.strip(), Last_Name.strip()))

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
        #Asks for driver's name, speed limit of the road and the speed of the driver's car
        while True:
            try:
                First_Name = str(input("DRIVER'S FIRST NAME: \n")).upper()
                if not re.match("^[A-Z]{1,20}$", First_Name):
                    print("ENGLISH ALPHABET ONLY | MAX 20 CHARACTERS")
                else:
                    Last_Name =  str(input("DRIVER'S LAST NAME: \n")).upper()
                    if not re.match("^[A-Z]{1,20}$", Last_Name):
                        print("ENGLISH ALPHABET ONLY | MAX 20 CHARACTERS")
                    else:
                        SpeedLimit = int(input("ROAD SPEED LIMIT: \n"))
                        CarSpeed = int(input("DRIVER'S SPEED: \n"))
                        assert 0 < CarSpeed < 300
                        addtolist(CarSpeed, SpeedLimit, fine)
                        wanted(First_Name, Last_Name)
                        break
            except ValueError:
                print("PLEASE ENTER APPROPRIATE VALUE")
            except AssertionError:
                print("PLEASE ENTER VALUES BETWEEN 0-300 KMS")
#Both of these function run in the while True: loop as they will keep adding to the fine list and checking for wanted drivers.
    elif task == "2":
            if sum(finelist) == 0:
                print("NO RECORDS")
            else:
                summary()
            print("TOTAL FINE AMOUNT: {}".format(sum(finelist)))
            time.sleep(1)
            print("AMOUNT OF FINES: {}".format(len(finelist)))
    elif task == "3":
        exit()
    else:
        print("INPUT VALUE NOT ALLOWED | ENTER NUMBER ONLY")
