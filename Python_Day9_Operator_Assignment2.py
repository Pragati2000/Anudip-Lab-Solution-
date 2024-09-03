#Write a Python program to remove duplicate characters of a given string.

#Input = “String and String Function” 

#Output: String and Function


def remove_duplicate_words(input_string):
    words = input_string.split()
    seen = set()
    result = []

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    
    return ' '.join(result)

# Input String
input_string = "String and String Function"

# Remove duplicate words
output_string = remove_duplicate_words(input_string)

print("Output:", output_string)


#Output:String and Function
