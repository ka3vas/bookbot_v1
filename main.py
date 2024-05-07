def main():
    letters_count = {"a": 0}

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    # num_words = count_words(text)
    # print(f"{num_words} words found in the document")

    print(letters_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

# this function could be called get_num_words
def count_words(string):
    return len(string.split())

main()