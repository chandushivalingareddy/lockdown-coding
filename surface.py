# Python Program to find Surface areas of cylinder and cone
# Importing Math library for value Of PI 
import math 
pi = math.pi 
radius = float(input('Please Enter the Radius: '))
height = float(input('Please Enter the Height: '))
slat_height = float(input('Please Enter the slat_height: '))

# Function To Calculate Surface Area of Cone 
def surfacearea(r, h): 
    return pi * r * s + pi * r * r; 
 

# Function To Calculate Surface Area of Cylinder
def surfacearea(r, h): 
    return 2*pi*pow(r,2)*h

print( "Surface Area Of Cone : ", surfacearea(radius, slat_height) ) 
print( "Surface Area Of Cylinder : ", surfacearea(radius, height) ) 