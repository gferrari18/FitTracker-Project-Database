import os

def num(p):    #Function created to ensure user enters a number instead of other characters
    text = input(p)
    while text[0].isnumeric() == False:
        print("You must enter a number.")
        text = input(p)
    return text

def reg(n,m): #Function created to display past user entries
    f = open(userUP + ".txt", "r")
    if os.path.getsize(userUP + ".txt") > 0:
        print("Your previous " + n + " measurements were: ")
    for line in f:
        if line.startswith(m):
            print(line[2:].strip())
        else: continue
    f.close()


def app(m, n):
    f = open(userUP + ".txt", "a")
    f.write(m + n + "\n")
    f.close()

def average(m, n, o):
    f = open(userUP + ".txt", "r")
    avg = 0
    hm = 0
    for line in f:
        if line.startswith(n):
            hm = hm + float(line[2:].strip())
            avg = avg + 1
    resavg = hm / avg
    avgtot = (float(o) - float(resavg))
    print("Your " + m + " measurement average is: " + str(resavg))
    print("Compared to your average, your " + m + " measurement difference is: " + str(avgtot))
    f.close()



usertype = input("Have you registered before? (type Yes or No): ")
usertypeUP = usertype.upper()

while usertypeUP != "YES" and usertypeUP != "NO": #loop created to ensure user types either yes or no
    print("Sorry, I do not understand. Please type Yes, No, or back to return to the previous menu")
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
   
    print("Welcome, " + user.capitalize() + ".")

weight = num("Please enter your weight: ")
reg("weight", "1-")
waist = num("Please enter your waist measurement: ")
reg("waist", "2-")
arms = num("Enter your arm (biceps/triceps) measurement: ")
reg("arms", "2-")
thighs = num("Enter your thigh measurement: ")
reg("thighs", "4-")

app("1-",weight)
app("2-",waist)
app("3-",arms)
app("4-",thighs)

average("weight", "1-",weight )
average("waist", "2-",waist)
average("arms", "3-",arms)
average("thighs", "4-",thighs)