def sort_on(letters):
    return letters["num"]

def word_count(book_text):
    word = book_text.split()
    num_words = len(word)
    return num_words

def charachter_count(book_text):
    text = book_text.lower()
    count = {}
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

def sort_count(dct):
    dict_list = []
    for i in dct:
        dict_list.append({"char": i, "num": dct[i]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
        
