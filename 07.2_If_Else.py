'Determime if a triangle inputed by user is Scalene, Isosceles, or Equilateral'

# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have same the lengths.
# Equilateral triangle: All sides are equal.

# Prompt user to enter 3 sides of the triangle.
a = int(input("The length of Side a = "))
b = int(input("The length of Side b = "))
c = int(input("The length of Side c = "))

if a != b and b != c and a !=c:     # If a does not equal b and does not equal 
    print("Scalene triangle")

elif a == b and b== c:
    print("Equilateral triangle")

else:
    print("Isosceles triangle")
    