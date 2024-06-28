def main():
    path = 'books/frankenstein.txt'
    book_text = get_book_text(path)
    book_word_count = word_count(book_text)
    book_char_count = char_count(book_text)
    sorted_char_dict = sort_char_dict(book_char_count)
    print_report(path, book_word_count, sorted_char_dict)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    
    for char in text:
        char_lower = char.lower()
        if char_lower in chars:
            chars[char_lower] += 1
        else:
            chars[char_lower] = 1
    return chars

def sort_char_dict(char_dict):
    dict_list = []

    for entry in char_dict:
        dict_list.append({
            "char": entry,
            "count": char_dict[entry]
        })

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def print_report(book, word_count, char_dict):
    print(f"------- Begin report of {book} -------")
    print(f"{word_count} many words found in document")
    print()

   
    for entry in char_dict:
        if entry['char'].isalpha():
            print(f"The '{entry['char']}' character was found {entry['count']} times")

    print()
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

main()