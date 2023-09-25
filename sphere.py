# Follow the instructions on the Variables and Expressions sheet to calculate the volume of a sphere with
# a given radius. As a hint, when doing something to the 3rd power, Python has a special operator. r^3 will NOT work.
radius = input("What is the circle's radius?")
pi = 3.14
volume = 4/3*pi*int(radius)**3
print("The volume of a sphere with radius", radius, "is", volume)