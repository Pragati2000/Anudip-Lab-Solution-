#Write a Python program to find duplicate values from a list and display those

def find_duplicates(items):
    duplicates = []
    seen = set()

    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)

    return duplicates

# Example usage:
my_list = [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 5]
duplicates = find_duplicates(my_list)
print("Duplicate values are:", duplicates)


#Output:Duplicate values are: [2, 4, 5]
