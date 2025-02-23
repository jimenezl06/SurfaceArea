import math

counter = 0
doWeLoop = True
r = 0
h = 0
cal_type = ''

def cone_surface_area(r,h):
    return ((math.pi * r * r) + (math.pi * r * math.sqrt(r*r + h*h)))

def cone_volume(r,h):
    return ((1.0/3) * math.pi * r * r * h)

def get_input():
    cal_type = input("Do you want Volume or Surface Area (V/S): ")
    r = float(input("Enter the radius (NN.NN) in feet: "))
    h = float(input("Enter the height (NN.NN) in feet: "))
    return cal_type, r, h


print("This program calculates the surface area and volume of a cone")

while (doWeLoop and counter < 3):

   usr_input = input("Do you want a calculation? Y/N: ")

   if(usr_input == 'Y' or usr_input == 'y'):

       cal_type, r, h = get_input()

       if cal_type == 'V' or cal_type == 'v':
           print("Cone volume is: " + str(round(cone_volume(r,h),2)))
       if cal_type == 'S' or cal_type == 's':
           print("Cone Surface Area is: " + str(round(cone_surface_area(r,h),2)))
   elif (usr_input == "N" or usr_input == "n"):
       doWeLoop = False
   else:
       if(counter < 2):
           print("Invalid Choice, try again!")
       counter = counter + 1

if counter == 3:
    print("Maximum Tries Exceeded - Try again later")
else:
    print("Program has stop.")