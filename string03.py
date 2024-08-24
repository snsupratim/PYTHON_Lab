# Input the number of lines
n = int(input("Enter the number of lines: "))

# Initialize an empty list to store the lines
lines = []

# Read the lines and capitalize them
for i in range(n):
    line = input("Enter a sentence: ")
    capitalized_line = line.upper()
    lines.append(capitalized_line)

# Print the capitalized lines
for line in lines:
    print(line)
