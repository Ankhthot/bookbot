import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # CLI argument for book path
    text = get_book_text(book_path)

    # Word count
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    # Character counts
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)

    # Print sorted character counts
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

main()

