usertype = input("Have you registered before? (type Yes or No)
usertypeUP = usertype.upper()
                
if usertypeUP != "YES":
                 print("Hello, " + usertype + ". I will create your profile")
                 f = open(usertypeUP + ".txt", "w")
                 f.write(usertype + "/n")
else:
                 f = open(usertypeUP + ".txt", "r")
                 print("Welcome back, " + f.print(firstline()))
   
