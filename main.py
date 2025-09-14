## Bookbot

from stats import get_book_text
from stats import count_words
from stats import count_chars


## main calls functions to count words in book
def main(book_path):
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")
    print(count_chars(book_text))


## Call main
main("books/frankenstein.txt")
