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
fines = [(45, 630),(40, 510),(35, 400),(30, 300),(25, 230),(20, 170),(15, 120),(10, 80),(0, 30)]
finelist = []

def compute_fine(CarSpeed, SpeedLimit, fine):
    over = CarSpeed - SpeedLimit
    for SpeedLimit, fine in fines:
        if over > SpeedLimit:
            print("{}$ Fine".format(fine))
    return 0


#Functions
def addtolist(CarSpeed, SpeedLimit, fine):
    if fine > 0:
        print("${} FINE".format(fine))
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
            compute_fine(CarSpeed, SpeedLimit, fine)
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
