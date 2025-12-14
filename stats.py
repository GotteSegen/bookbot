def num_of_words(book_text: str):
    list_words = book_text.split()
    total_words = len(list_words)
    return total_words

def num_of_characters(book_text: str):
    # Return the number of times each character appears in the str
    # For each character in the book
    char_count = {}
    text = book_text.lower()
    for char in text:
        if char in char_count:
             char_count[char] += 1
        else:
             char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_dict(char_count: dict):
    char_list = []
    for char in char_count:
        char_list.append({"chars" : char, "num" : char_count[char]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list