# Input the comma-separated sequence of words
input_string = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
words = input_string.split(', ')

# Sort the words alphabetically
sorted_words = sorted(words)

# Join the sorted words back into a comma-separated string
sorted_string = ', '.join(sorted_words)

# Print the sorted string
print(sorted_string)
