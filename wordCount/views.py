from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html',)

def abouts(request):
    return render(request, 'About.html',)

def valid(request):
    Counting = request.GET['feedback']

    wordList = Counting.split()
    wordDictionary = {}

    for words in wordList:
        if words in wordDictionary:
            wordDictionary[words] +=1
        else:
            wordDictionary[words] =1

    sortedlist = sorted(wordDictionary.items(), key= operator.itemgetter(1), reverse= True)

    return render(request, 'count.html', {'feedback': Counting, 'count':len(wordList), 'wordDict': sortedlist })
