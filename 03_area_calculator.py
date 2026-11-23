import math
print("1.Rectangle  2.Square  3.Circle  4.Triangle")
choice = int(input("Choose shape: "))
if choice == 1:
    l = float(input("Length: "))
    w = float(input("Width: "))
    area = l * w
elif choice == 2:
    s = float(input("Side: "))
    area = s ** 2
elif choice == 3:
    r = float(input("Radius: "))
    area = math.pi * r ** 2
elif choice == 4:
    b = float(input("Base: "))
    h = float(input("Height: "))
    area = 0.5 * b * h
else:
    area = None
if area is None:
    print("Invalid choice")
else:
    print("Area:", round(area, 2))
