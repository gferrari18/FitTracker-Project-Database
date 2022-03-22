'''
def num(text):
    if text.isnumeric() == False:
        print("You must enter a number.")

hue = input("eae ")

num(hue)
'''



myfile = open("nice.txt", "r")
myline = myfile.readline()
print(myline)
myfile.close()

