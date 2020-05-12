from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request, 'home.html')

def count(request):
    fulltext= request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word.lower() in worddictionary:
            #increment count
            worddictionary[word.lower()] += 1
        else:
            #add to the dictionary
            worddictionary[word.lower()]=1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse= True)

    return render(request, 'Count.html', {'fulltext':fulltext,
    'count': len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')
