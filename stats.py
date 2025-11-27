def get_num_words(read):
    read = read.split()
    num_words = len(read)
    return num_words

def count_letters(book):
    
    letter_count = {}
    book = book.lower()

    for letter in book:
        if letter.isalpha():
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1        
        
    return letter_count

def sorted_dict(dictionary):
    list_of_dict = []
    
    for letter, count in dictionary.items(): 
        temp_dict = {"char": letter, "num": count}
        list_of_dict.append(temp_dict)
   
    def order_by(num):
       return num["num"]
    list_of_dict.sort(reverse=True, key = order_by)
   
    return list_of_dict



