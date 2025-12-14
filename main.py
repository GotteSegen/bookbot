# Import num_of_words function from stats.py
import sys
from stats import num_of_words, num_of_characters, sort_dict

def get_book_text(file_path: str):
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents

def main():
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            book_file_path = sys.argv[1]

        # Get contents of book
        contents = get_book_text(book_file_path)

        # Determine total words in book
        total_words = num_of_words(contents)

        # Determine total characters in book
        total_chars = num_of_characters(contents)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")

        sorted_library = sort_dict(total_chars)

        for dict in sorted_library:
            if dict["chars"].isalpha():
                char = dict["chars"]
                num = dict["num"]
                print(f"{char}: {num}")

if __name__ == "__main__":
    main()