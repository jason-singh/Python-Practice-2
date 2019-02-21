#problem1.py
#Doing onenote problem1 that the teacher has given us
#Jason Singh, 12 February

import time

def cardbalance(z,purchase,y,x):
    print("Intial Card Balance:{}".format(z))
    time.sleep(1)
    print("Name of purchase: {}".format(purchase))
    time.sleep(1)
    print("Cost of purchase: {}".format(round(y,2)))
    time.sleep(1)
    x = z - y
    print("New Balance: {}".format(round(x,2)))

x = 0
z = int(input("What is your intital card balance? "))
purchase = input("What is your purchase's name? ")
y = float(input("How much did your purchase cost? "))

cardbalance(z,purchase,y,x)
