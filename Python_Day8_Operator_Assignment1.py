#Write a Python program to count the occurrences of each word in a given sentence 

#string = “To change the overall look of your document. To change the look available in the gallery” 


import string

def count_word_occurrences(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Remove punctuation from the sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Split the sentence into words
    words = sentence.split()
    
    # Create a dictionary to count occurrences
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Count the occurrences of each word
word_occurrences = count_word_occurrences(sentence)

# Print the results
for word, count in word_occurrences.items():
    print(f"'{word}': {count}")


""" Output:
         'to': 2
         'change': 2
         'the': 3
         'overall': 1
         'look': 2
         'of': 1
         'your': 1
         'document': 1
         'available': 1
         'in': 1
         'gallery': 1 """
