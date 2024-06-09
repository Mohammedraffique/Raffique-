def remove_consonants(string):
    vowels = "aeiouAEIOU"
    consonants_removed = "".join(char for char in string if char in vowels)
    return consonants_removed

input_string = input("Enter a string: ")
result = remove_consonants(input_string)
print("String with consonants removed:", result)
