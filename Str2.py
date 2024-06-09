def replace_first_occurrence(string, old_char, new_char):
    for i, char in enumerate(string):
        if char == old_char:
            return string[:i] + new_char + string[i+1:]
    return string

original_string = "hello world"
old_character = "l"
new_character = "z"
modified_string = replace_first_occurrence(original_string, old_character, new_character)
print("Modified string:", modified_string)
