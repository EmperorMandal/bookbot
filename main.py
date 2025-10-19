
from stats import get_num_words
from stats import count_carecters


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("/home/peter/workspace/github.com/EmperorMandal/bookbot/bookbot/books/frankenstein.txt")
    #return print(f"{book}")
    return book


print(f" Found {get_num_words(main())} total words")
print(count_carecters(main()))
