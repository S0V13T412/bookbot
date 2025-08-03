import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

from stats import word_count
from stats import charachter_count
from stats import sort_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = word_count(text)
        num_char = charachter_count(text)
        sorted_list = sort_count(num_char)
    #print(f"{num_words} words found in the document")
    #print(num_char)
    #print(sort_count(num_char))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in sorted_list:
            i_char = i["char"]
            i_num = i["num"]
            print(f"{i_char}: {i_num}")
        print("============= END ===============")

main()
