def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    num_words = count_words(text)
    letters_count = count_letters(text)

    print(letters_count)

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
        sign_lower = sign.lower()
        
        if sign_lower in dictionary:
            dictionary [sign_lower] += 1
        else:
            dictionary [sign_lower] = 1

    return dictionary        

main()