from django.shortcuts import render
from dictionary import words
from dictionary import dictionary
from django.contrib import messages
from dictionary import anagram_checker

def IndexPage(request):
    if request.method == "POST":
        #word subset view
        worda = request.POST.get('word')
        final_words = words.all_real_combinations(worda)
        final_words_count = len(final_words)
       # wordiii = request.POST.get('wordish')
        context = {'final': final_words, 'words' : worda, 'count': final_words_count}
        return render(request, "main/index.html", context)      
    return render(request, "main/index.html")

def DictionarySearch(request):
    if request.method == "POST":
        wordb = request.POST.get('word_search')
        result_of_search = dictionary.the_dictionary(wordb)
        anagram_check = anagram_checker.check_anagram(wordb)
        if anagram_check == list():
            messages.warning(request, f"{wordb} does not have any anagrams")
        context = {'result':result_of_search, 'word':wordb.lower().strip(), "anagram":anagram_check, 'dictionary':dictionary.my_dictionary}
        return render(request, "main/DictionarySearch.html", context)
    return render(request, "main/DictionarySearch.html")
