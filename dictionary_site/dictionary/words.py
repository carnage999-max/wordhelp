from itertools import permutations

#import the dictionary.py file
from .dictionary import my_dictionary


def all_real_combinations(word):
    all_word_list = list()
    i = len(word)
    while i <= len(word):
        #make sure that single characters (like 'a', 'f', 'j'...)are not included
        if i == 1:
            break
         #get all permutations of the word
        all_word_list += list("".join(p) for p in permutations(word, i))
        i -= 1
     #make the list contain non-repeated values
    all_word_list = set(all_word_list)
    
    #real_world_list contains permutations of the word that are in the dictionary
    real_word_list = list()
    for words in list(all_word_list):
        if words in my_dictionary:
            real_word_list.append(words)
    return real_word_list