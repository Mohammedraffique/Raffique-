def count_characters(string):
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
    for char, freq in char_freq.items():
        print(f"{char}: {freq}")


input_string = "hello world"
count_characters(input_string)


