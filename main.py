from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open (sys.argv[1]) as file:
        text = file.read()
    return text




def main():
    word_count = count_words(get_book_text())
    directory_characters = count_characters(get_book_text())
    sorted_characters = sort_characters(directory_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for character, count in sorted_characters:
        print(f'{character}: {count}')
    print("============= END ===============")
main()