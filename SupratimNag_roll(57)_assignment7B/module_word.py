# Function to create a word frequency dictionary from a string
def create_word_frequency_dict(input_string):
    # Split the input string into words
    words = input_string.split()

    # Initialize an empty dictionary to store word frequencies
    word_freq_dict = {}

    # Iterate through the words
    for word in words:
        # Remove punctuation and convert to lowercase for uniformity
        word = word.strip('.,!?()[]{}":;')
        word = word.lower()

        # Check if the word is already in the dictionary
        if word in word_freq_dict:
            # Increment the word's frequency by 1
            word_freq_dict[word] += 1
        else:
            # Add the word to the dictionary with a frequency of 1
            word_freq_dict[word] = 1

    return word_freq_dict


def find_first(input_string):
    return input_string[0]


def find_last(input_string):
    return input_string[-1]
