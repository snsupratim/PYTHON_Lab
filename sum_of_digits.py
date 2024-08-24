# 5.sum of a number digit
# Input from the user
num = int(input("Enter an n-digit number: "))

# Initialize a variable to store the sum of digits
digit_sum = 0

# Convert the number to a string to process each digit
num_str = str(num)

# Iterate through each digit in the number
for digit_char in num_str:
    digit = int(digit_char)
    digit_sum += digit

print(f"The sum of the digits of {num} is {digit_sum}.")