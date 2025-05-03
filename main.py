from stats import get_num_words
from stats import letter_count

def get_book_text(f):
    with open(f, encoding="utf8") as frank:
        return frank.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(len(text))
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    letters = letter_count(text)
    print(letters)
    print("done")

main()
