# Accept the input sentence from the user
sentence = input("Enter a sentence: ")

# Initialize counters for uppercase and lowercase letters
uppercase_count = 0
lowercase_count = 0

# Iterate through each character in the sentence
for char in sentence:
    # Check if the character is an uppercase letter
    if char.isupper():
        uppercase_count += 1
    # Check if the character is a lowercase letter
    elif char.islower():
        lowercase_count += 1

# Print the counts
print(uppercase_count, lowercase_count)
