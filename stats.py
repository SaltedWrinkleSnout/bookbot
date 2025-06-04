def word_counter(book):
    # counts and returns the number of words in a string
    words = book.split()
    num_words = len(words)
    return num_words

def char_count(book):
    # counts the characters in the string
    book_lower = book.lower()
    counter = {
        "": 0
    }
    math = 0
    #print(book_lower)
    for char in book_lower:
        present = char in counter
        if present == False:
            counter[char] = 1
        else:
            current = counter[char]
            update = current + 1
            counter[char] = update       
    return counter

def report(dictionary):
    def sort_on(dict):
        return dict["num"]
    report_list = []
    for character in dictionary:
        num = dictionary[character]
        new_dict = {"char" : character, "num": num}
        report_list.append(new_dict)
    #print(report_list)
    report_list.sort(reverse=True, key=sort_on)
    #print(report_list)
    return report_list

