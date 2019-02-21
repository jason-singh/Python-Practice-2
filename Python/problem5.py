#problem5.py
#Doing onenote problem 5 that the teacher has given us
#Jason Singh, 14 February


#Lists
TenDemerit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TwentyDemerit = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ThirtyFiveDemerit = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
FourtyDemerit = [31, 32, 33, 34, 35]
Demerits = [10, 20, 35, 40 ,50]

#Variables
FifteyDemerit = 36

#Find out the speed limit of the current road
SpeedLimit = int(input("What is the Speed Limit of this road? \n"))

CarSpeed = int(input("How fast was the driver driving his vehicle? \n"))
CarOverLimit = CarSpeed - SpeedLimit
if CarOverLimit in TenDemerit:
    print("You have gained {} demerits".format(Demerits[0]))
elif CarOverLimit in TwentyDemerit:
    print("You have gained {} demerits".format(Demerits[1]))
elif CarOverLimit in ThirtyFiveDemerit:
    print("You have gained {} demerits".format(Demerits[2]))
elif CarOverLimit in FourtyDemerit:
    print("You have gained {} demerits".format(Demerits[3]))
elif CarOverLimit >= FifteyDemerit:
    print("You have gained {} demerits".format(Demerits[4]))
else:
    print("You have not gained any demerits. Drive Safe")
