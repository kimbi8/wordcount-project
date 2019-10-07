#have to give back a http response?
from django.http import HttpResponse
# django code that allows us to return someinformation
# as http resoponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#def home(request):
#    return render(request, 'home.html', {'hithere':'This is me.'})
#    return render(request, 'home.html', {'hithere':'This is me.'})
# above just shows that the render function can also take in a dictionary

#def eggs(request):
#    return HttpResponse('Eggs are great!')
#html code should be put in a seperate template

def count(request):
    fulltext = request.GET['fulltext'] # inside GET we put the parameter as shown in the url count page which is 'fulltext'

    wordlist = fulltext.split() #splits into individual words
                                #wordlist = list of words
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1 #increase
        else:
            worddictionary[word] = 1 #add to the worddictionary
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    #worddictionary.items() coverts dictionary into a wordlist
    #key=operator.itemgetter(1) gets the nth element which is the keyvalue i.e counts
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords': sortedwords })



# this page sends u to the html templates based on what url u specify
# ex. kimbi.com/count sends u to count html page
