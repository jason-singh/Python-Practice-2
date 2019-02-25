#speedingticket.py
#Trying to make a efficient and small script that can be used to track illegial drivers.
#Jason Singh, 21 February

#Modules
import time

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
                            "20": 170,
                            "24": 230,
                            "29": 300,
                            "34": 400,
                            "39": 510,
                            "44": 630}

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
                for i in range(0, len(speedlist)):
                    print("FIRST NAME: {}".format(firstlist[i]))
                    print("LAST NAME: {}".format(lastlist[i]))
                    print("OVERSPEEDING BY: {} km".format(speedlist[i]))
            print("TOTAL FINE: {}".format(sum(finelist)))
            time.sleep(1)
            print("TOTAL AMOUNT OF FINES: {}".format(len(finelist)))
    elif task == "3":
        exit()
    else:
        print("INPUT VALUE NOT ALLOWED")
