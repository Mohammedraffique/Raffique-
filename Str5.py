def are_strings_equal(str1, str2):
    return str1 == str2


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_strings_equal(string1, string2):
    print("The strings are equal.")
else:
    print("The strings are not equal.")
