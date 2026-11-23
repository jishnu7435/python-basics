print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter choice: "))
if choice == 1:
    f = float(input("Fahrenheit: "))
    print("Celsius:", (f - 32) * 5 / 9)
elif choice == 2:
    c = float(input("Celsius: "))
    print("Fahrenheit:", c * 9 / 5 + 32)
else:
    print("Invalid choice")
