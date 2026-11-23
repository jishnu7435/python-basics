n = int(input("Number of elements: "))
numbers = []
for _ in range(n):
    numbers.append(int(input("Enter number: ")))
even_count = sum(1 for number in numbers if number % 2 == 0)
odd_count = len(numbers) - even_count
print("Numbers:", numbers)
print("Even count:", even_count)
print("Odd count:", odd_count)
