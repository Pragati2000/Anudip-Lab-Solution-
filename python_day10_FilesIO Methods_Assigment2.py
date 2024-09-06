# Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(filename):
    """
    Counts the total number of words in a text file and displays the count.

    :param filename: Name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The file '{filename}' contains {word_count} words.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
count_words_in_file("ABC.txt")

#Output:The file 'ABC.txt' contains 15 words.
