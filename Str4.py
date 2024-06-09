def string_length(string):
    return len(string)

def string_copy(string):
    return string[:]

def string_concatenate(string1, string2):
    return string1 + string2

def string_to_uppercase(string):
    return string.upper()

def compare_strings(string1, string2):
    return string1 < string2

s1 = "hello"
s2 = "world"

print("Length of string:", string_length(s1))
print("Copy of string:", string_copy(s1))
print("Concatenated string:", string_concatenate(s1, s2))
print("Uppercase string:", string_to_uppercase(s1))
print("Comparing strings for alphabetical order:", compare_strings(s1, s2))
