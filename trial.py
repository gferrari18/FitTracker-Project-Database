from curses.ascii import isalpha
import os

def num(text):
    while text.isnumeric() == False:
        print("You must enter a number.")
        text = input("Enter your " + text + "using numbers")


usertype = input("Have you registered before? (type Yes or No): ")
usertypeUP = usertype.upper()

while usertypeUP != "YES" and usertypeUP != "NO": #loop created to ensure user types either yes or no
    print("Sorry, I do not understand. Please type Yes or No")
    usertype = input("Have you registered before? (type Yes or No): ")
    usertypeUP = usertype.upper()

if usertypeUP == "YES":
    user = input("Please enter your name: ")
    userUP = user.upper()
    f = open(userUP + ".txt", "a") #if start with "r", will give an error if file does not exist
    f.close()
    f = open(userUP + ".txt", "r")
    while f.readline() == "": #loop created to ensure file exists. loop will exit once an user with the name of a created file is typed.
        print("This name does not seem to be registered. Try rewriting your name.")
        f.close()
        os.remove(userUP + ".txt")
        user = input("Please enter your name: ")
        userUP = user.upper()
        f = open(userUP + ".txt", "a")
        f.close
        f = open(userUP + ".txt", "r")
    f.close()
    print("Welcome back, " + user.capitalize() + ".")

                                 
elif usertypeUP == "NO": #creates file for new user
    user = input("Please enter your name: ")
    userUP = user.upper()
    f = open(userUP + ".txt", "a")
    f.close()
    f = open(userUP + ".txt", "r")
    while f.readline() != "": #this loop ensure another file with the same name does not exist
        f.close()
        print("This name is already in use. Please use a different one.")
        user = input("Please enter your name: ")
        userUP = user.upper()
        f = open(userUP + ".txt", "a")
        f.close()
        f = open(userUP + ".txt", "r")
    f.close()
    f = open(userUP + ".txt", "a")
    f.write(user + "\n")

    print("Welcome, " + user.capitalize() + ".")




weight = input("Please enter your weight: ")
while weight.isalpha():
    print("You must enter a number.")
    weight = input("Enter it now using numbers: ")

waist = input("Please enter your waist measurement: ")
while waist.isalpha():
    print("You must enter a number.")
    waist = input("Enter it now using numbers: ")

arms = input("Enter your arm (biceps/triceps) measurement: ")
while arms.isalpha():
    print("You must enter a number.")
    arms = input("Enter it now using numbers: ")

thighs = input("Enter your thigh measurement: ")
while thighs.isalpha():
    print("You must enter a number.")
    thighs = input("Enter it now using numbers: ")

measurements = (weight, waist, arms, thighs) #placing measurements into a tuple

