import json

with open('dictionary/dictionary.json') as f:
        my_dictionary = json.load(f)
def the_dictionary(search):
    return my_dictionary.get(search.lower().strip(), "Word not Found. Please check your word again")
