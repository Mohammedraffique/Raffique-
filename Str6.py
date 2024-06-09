def strcpy(source, destination):
    if not source:
        return destination
    else:
        return strcpy(source[1:], destination + source[0])


source_str = "Hello, World!"
destination_str = ""
copied_str = strcpy(source_str, destination_str)
print("Copied string:", copied_str)
