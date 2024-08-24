# Function to find common words between two strings
def find_common_words(string1, string2):
    # Split both strings into lists of words
    words1 = string1.split()
    words2 = string2.split()
    
    # Convert both lists to sets for efficient intersection
    set1 = set(words1)
    set2 = set(words2)
    
    # Find the common words using set intersection
    common_words = set1.intersection(set2)
    
    return list(common_words)

# Input two strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Find and print the common words
common_words = find_common_words(string1, string2)

if common_words:
    print("Common words:", common_words)
else:
    print("No common words found.")
