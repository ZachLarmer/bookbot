## Bookbot
import sys
from stats import get_book_text
from stats import count_words
from stats import count_chars
from stats import sorted_chars


## main calls functions to count words in book
def main(book_path):
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_frequencies = count_chars(book_text)
    char_report = sorted_chars(char_frequencies)
    print(f"============ BOOKBOT ============") 
    print(f"Analyzing book found at {book_path}t...") 
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char, count in char_report:
        print(f"{char}: {count}")
    print(f"============= END ===============")


## Call main
main("books/frankenstein.txt")
