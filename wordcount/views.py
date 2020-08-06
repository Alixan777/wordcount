from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def gallery(request):
    return HttpResponse("<h1 style= color:blue;>Welcome to my Django Gallery!</h1>")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddict={}

    for word in wordlist:
        if word in worddict:
            #Increment
            worddict[word] += 1
        else:
            #add the word to the dictionary!
            worddict[word] = 1
    sor = sorted(worddict.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{"fulltext":fulltext,"wordlist":len(wordlist),"worddict":sor})


def about(request):
    return render(request, 'about.html')
