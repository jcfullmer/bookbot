from stats import get_num_words
from stats import letter_count
from stats import sort_alpha

def get_book_text(f):
    with open(f, encoding="utf8") as frank:
        return frank.read()

def main():
    book_path = "books/frankenstein.txt"
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

'''def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(len(text))
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    letter_counted = letter_count(text)
    print(letter_counted)
    sorted = sort_alpha(letter_counted)
    print(sorted)
'''
main()
