import sys

def is_triangle(*args): # validade triangle
   if sum(sides[:-1]) <= sides[-1]:
      return False
      

def which_triangle(*args): # define triangle
   if (sides[0] == sides[1] and sides[1] == sides[-1]):
      return 1
   elif (sides[0] == sides[1] or sides[1] == sides[-1] or sides[0] == sides[-1]):
      return 2 
      

side = ""
sides = []

for lines in range(1,4): # reading three sides
    try:
       side = int(input(f"Enter with side {lines}: "))
    except ValueError:
        print("Invalid value, type a number")
        sys.exit(1)
    sides.append(side)
sides.sort()

if is_triangle(which_triangle(sides)) == False:
    print('\n Is not a Triangle')
    quit()
if which_triangle(sides) == 1: print("\n equilateral triangle")
elif which_triangle(sides) == 2: print("\n isosceles triangle")
else: print("\n scalene triangle")

