#problem3.py
#Doing onenote problem 3 that the teacher has given us
#Jason Singh, 12 February

def conversion(x):
    inch = x * 39.37
    print("In inches your height is: ", round(inch, 2))
    feet = x * 3.281
    print("In feet your height is ", round(feet,2))
    inchs = x * 3.281 % 1 * 12
    print("You are {} foot and {} inches".format(round(feet), round(inchs)))



x = float(input("How tall are you in meters? "))
conversion(x)
