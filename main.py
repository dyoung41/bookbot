from stats import get_num_words
from stats import count_letters
from stats import sorted_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f: 
        book = f.read()
    return book
    
def main():
    read = get_book_text(sys.argv[1])
    num_words = get_num_words(read)
    num_letters= count_letters(read)
    sd = sorted_dict(num_letters)

    print(f"============ BOOKBOT ============\nAnalyzing bookpy...\n----------- Word Count ----------\nFound {num_words} total words\n----------- Character Count ----------")

    for key_pair in sd:
        char = key_pair["char"]
        number = key_pair["num"]
        print(f"{char}: {number}")




main()   

