
import sys
from stats import get_num_words
from stats import count_carecters
from stats import sorting



print(sys.argv)

check = len(sys.argv)
if check != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
elif check == 2:
    book_path = sys.argv[1]



def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

#"/home/peter/workspace/github.com/EmperorMandal/bookbot/bookbot/books/frankenstein.txt"

def main():
    book = get_book_text(book_path)
    return book

def print_sorted_list(sort_list):

    for i in sort_list:
        charecter = i["char"]
        number = i["num"]
        
        if charecter.isalpha():
            print(f" {charecter}: {number}")
        
#print(count_carecters(main()))

list_char = count_carecters(main())
sort_list = sorting(list_char)
print("============ BOOKBOT ============")
print(f" Analyzing book found at {book_path}")
print("----------- Word Count ----------")
print(f" Found {get_num_words(main())} total words")
print("--------- Character Count -------")
print_sorted_list(sort_list)
print("============= END ===============")

