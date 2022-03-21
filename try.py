'''
def num(text):
    if text.isnumeric() == False:
        print("You must enter a number.")

hue = input("eae ")

num(hue)
'''



def num(text):
    while text.isnumeric() == False:
        print("You must enter a number.")
        text = input("Enter it now using numbers: ")

print("Let's get your measurements and compare it to last the last time you used this software.")
weight = input("Please enter your weight: ")
num(weight)
print(weight)
