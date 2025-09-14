## Bookbot functions

## book text to string
def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return(file_contents)


## main calls the read function and prints
def main():
    print(get_book_text())


## Call main
main()
