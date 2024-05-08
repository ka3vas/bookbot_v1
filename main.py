def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    num_words = count_words(text)
    letters_count = count_letters(text)

    print_report(book_path, num_words, letters_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

# this function could be called get_num_words
def count_words(string):
    return len(string.split())

# get_chars_dict
def count_letters(string):
    dictionary  = {}

    for sign in string:
        if sign.isalpha():
            sign_lower = sign.lower()
        
            if sign_lower in dictionary:
                dictionary[sign_lower] += 1
            else:
                dictionary[sign_lower] = 1

    return dictionary     

def sort_on(dict):
    return dict["num"]   

def print_report(book_path, num_words, letters_count):
    letter_list = []
    for x in letters_count.items():
        letter_list.append({"letter": x[0], "num": x[1]})

    letter_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words } words found in the document")
    for letter in letter_list:
        print(f"The '{letter['letter']}' character was found {letter['num']} times")
    print("--- End report ---")

main()