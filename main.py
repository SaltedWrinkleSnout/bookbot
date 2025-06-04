from stats import word_counter
from stats import char_count
from stats import report

def get_book_text(filepath):
    # a function that takes a filepath and returns the contents of the file as a string
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    
    book_contents = get_book_text("books/frankenstein.txt")
    #print(book_contents)
    
    num_of_words = word_counter(book_contents)
    #print(num_of_words)
    
    message = f"{num_of_words} words found in the document"
    #print(message)
    
    count = char_count(book_contents)
    #print(count)
    
    report_list = report(count)
    #print(report_list)

    #final formatted report
    print("============ BOOKBOT ============")
    print("Analyzing book found at" + book_path + "...")
    print("----------- Word Count ----------")
    print("Found", num_of_words, "total words")
    print("--------- Character Count -------")
    
    for key in report_list:
        symbol = key["char"]
        total = key["num"]
        line = f"{symbol}: {total}"
        if symbol.isalpha() == True:
            print(line)
        #print(key["num"])
        '''if key.isalpha() == True :
            print(f"{key}:{value}")'''

    print("============= END ===============")

    return

main()