def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    directory_characters = {}
    l_text = text.lower()
    for char in l_text:
        if char not in directory_characters:
            directory_characters[char] = 1
        else:
            directory_characters[char] += 1
    return directory_characters

def sort_characters(directory_characters):
    sorted_dict = []
    for char in directory_characters:
        if char.isalpha():
            sorted_dict.append((char, directory_characters[char]))
    sorted_characters = sorted(sorted_dict, key=lambda x: x[1], reverse=True)
    return sorted_characters