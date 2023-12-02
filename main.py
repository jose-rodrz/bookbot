import string

def main():
    path = "books/frankenstein.txt"
    book = get_book(path)
    letter_report = letter_counts(book)
    sorted_counts = sorted(letter_report, key=letter_report.get, reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{wordcount(book)} words found in the document\n")
    for l in sorted_counts:
        print(f"The '{l}' character was found {letter_report[l]} times")
    print("--- End report ---")

def get_book(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def wordcount(text):
    words = text.split()
    return len(words)

def letter_counts(text):
    alphabet = string.ascii_lowercase
    letters = list(text.lower())
    letter_counts = {}

    for letter in alphabet:
        letter_counts[letter] = letters.count(letter)
    return letter_counts

main()


    