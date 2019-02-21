#listintro.py
#Learning about the list function in python, on OneNote.
#Jason Singh, 19 February

classsize = 4

names = ["Aryan","Jason","Hanro","William","Robert"]
marks = [98,96,92,85,76]

def printing(names):
    for i in range(len(names)):
        print("Names {}: {} | Grade: {}".format(i + 1, names[i], marks[i]))




print("_____________________________________________")

printing(names)

print("_____________________________________________")

print("Enter Y if you want to enter more students or N to terminate application")
add = input("Enter Y or N: \n")
if add == "Y":
    for i in range(classsize):
        names = names + [input("Enter Name:")]
        marks = marks + [input("Enter Grade:")]
    printing(names)
elif add == "N":
    exit()
