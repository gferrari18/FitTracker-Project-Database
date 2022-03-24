# opening the file in read mode
file = open("motivation.txt", "r")
replacement = ""
# using the for loop
for line in file:
    line = line.strip()
    changes = line.replace("hardships", "situations")
    replacement = replacement + changes + "\n"

file.close()
# opening the file in write mode
fout = open("motivation.txt", "w")
fout.write(replacement)
fout.close()