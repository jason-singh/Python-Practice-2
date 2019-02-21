#speedingticket.py
#Trying to make a efficient and small script that can be used to track illegial drivers.
#Jason Singh, 21 February

wanted_first = ["James", "Helga", "Zachary"]
wanted_last = ["Wilson", "Norman", "Conroy "]
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

def wanted(First_Name, Last_Name):
    if First_Name in wanted_first and Last_Name in wanted_last:
        print("{} {} has an arrest warrant for his name".format(First_Name, Last_Name))
    else:
        print("{} {} has no arrset warrant for his name".format(First_Name, Last_Name))
speederlist = []

First_Name = input("What is the driver's First Name: \n")
Last_Name =  input("What is the driver's Last Name: \n")
SpeedLimit = int(input("What is the speed limit: \n"))
CarSpeed = int(input("What was the drivers speed: \n"))


CarOverLimit = CarSpeed - SpeedLimit
if CarOverLimit in a:
    print("You have to pay $30")
elif CarOverLimit in b:
    print("You have to pay $80")
elif CarOverLimit in c:
    print("You have to pay $120")
elif CarOverLimit in d:
    print("You have to pay $170")
elif CarOverLimit >= e:
    print("You have to pay $230")
elif CarOverLimit in f:
    print("You have to pay $300")
elif CarOverLimit in g:
    print("You have to pay $400")
elif CarOverLimit in h:
    print("You have to pay $510")
elif CarOverLimit >= i:
    print("You have to pay $630")
else:
    print("You have no fine to pay. Drive Safe")

wanted(First_Name, Last_Name)
