# 3. pallindrome number

# Input from the user
num = int(input("Enter a number: "))

# Store a copy of the original number
original_num = num

# Initialize a variable to store the reversed number
reverse_num = 0

# Reverse the number
while num > 0:
    # Extract the last digit
    last_digit = num % 10
    
    # Add the last digit to the reverse number in the reverse order
    reverse_num = reverse_num * 10 + last_digit
    
    # Remove the last digit from the original number
    num = num // 10

# Check if the reversed number is equal to the original number
if original_num == reverse_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")