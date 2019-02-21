#problem2.py
#Doing onenote problem2 that the teacher has given us
#Jason Singh, 12 February


#Define the module/function
def cupsneeded(x):
    #create a formulae that figures out how many cups are needed
    cups = x / 125
    #print out the number of cups needed after user enters amount of flour in grams
    print("The number of cups needed are: ", cups)

#ask user for the number of flour in grams
x = int(input("How many grams of flour do you have? "))\
#run the module/function with the parameter "x" which is number of flour
cupsneeded(x)
