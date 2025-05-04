from stats import get_num_words
from stats import letter_count
from stats import sort_alpha
import sys

def get_book_text(f):
    with open(f, encoding="utf8") as frank:
        return frank.read()

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counted = letter_count(text)
    sorted_chars = sort_alpha(letter_counted)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print if it's an alphabetical character
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    main()
