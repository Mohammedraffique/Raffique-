def remove_repeated_chars(string):
    return "".join(dict.fromkeys(string))
input_string = "hello"
output_string = remove_repeated_chars(input_string)
print(output_string)  # Output will be "helo"
