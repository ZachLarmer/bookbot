

## book text to string
def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return(file_contents)

## count each word in the text string
def count_words(contents):
    content_list = contents.split()
    num_words = len(content_list)
    return num_words

## count characters
def count_chars():
    char_frequencies = {}
    book_text = get_book_text()
    chars = book_text.lower()
    for char in chars:
        if char in char_frequencies:
            char_frequencies[char] +=1
        else:
            char_frequencies[char] = 1
    return char_frequencies
    