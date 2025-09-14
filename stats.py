

## book text to string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)

## count each word in the text string
def count_words(contents):
    content_list = contents.split()
    num_words = len(content_list)
    return num_words

## count characters
def count_chars(book_text):
    char_frequencies = {}
    chars = book_text.lower()
    for char in chars:
        if char.isalpha():
            if char in char_frequencies:
                char_frequencies[char] +=1
            else:
                char_frequencies[char] = 1
    return char_frequencies

## sort and format character counts
def sorted_chars(char_frequencies):
    sorted_dict = sorted(char_frequencies.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict