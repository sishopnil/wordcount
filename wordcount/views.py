from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    word_dic = {}

    for word in wordlist:
        if word in word_dic:
            # increase
            word_dic[word] += 1
        else:
            # add to the dictionary
            word_dic[word] = 1

    sorted_words = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sorted_words': sorted_words})
