# Input from the user
num = int(input("Enter a number: "))

# Convert the number to a string to calculate the number of digits
num_str = str(num)

# Calculate the number of digits
num_digits = len(num_str)

# Initialize a variable to store the sum of the digits raised to the power of num_digits
sum_of_powers = 0

# Iterate through each digit in the number
for digit_char in num_str:
    digit = int(digit_char)
    sum_of_powers += digit ** num_digits

# Check if the sum of the powers is equal to the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")