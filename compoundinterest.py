# Python program to find compound interest 

p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
n = float(input("Enter the value of n : "))

# calculating compound interest
ci =  p * (pow((1 + r / 100), n)) 


# printing the values
print("Principle amount  : ", p)
print("Interest rate     : ", r)
print("value of n    : ", n)
print("compound Interest : ", ci)