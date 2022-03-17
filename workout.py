namlist = open("namelist.txt", "a")

print("Welcome to your personal, personal trainer")
user = input("Please, enter your name: ")
namlist.write(user + "\n")

namlist.close()

namelist = open("namelist.txt", "r")
filename = ""


for x in namelist:
        file = x.strip()
        if file == user:
            filename = file
            print("I will load your file")
if filename == '':
    
f = open(filename)
        
