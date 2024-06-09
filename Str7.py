def sort_string(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string


input_string = input("Enter a string: ")
sorted_string = sort_string(input_string)
print("Sorted string:", sorted_string)
