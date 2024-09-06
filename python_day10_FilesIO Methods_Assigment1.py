
#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file_line_by_line(filename):
    """
    Reads the content of a text file line by line and displays it on the screen.

    :param filename: Name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
read_file_line_by_line("ABC.txt")

"""Output:
          my name is pragati ganesh goregaonkar
          my age is 24
          and i live in goregaon """
