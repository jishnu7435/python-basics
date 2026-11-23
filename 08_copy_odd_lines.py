source = input("Source file path: ")
destination = input("Destination file path: ")
with open(source, "r", encoding="utf-8") as infile:
    with open(destination, "w", encoding="utf-8") as outfile:
        for line_number, line in enumerate(infile, start=1):
            if line_number % 2 == 1:
                outfile.write(line)
print("Odd-numbered lines copied successfully")
