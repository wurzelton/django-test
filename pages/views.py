from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs): #mit *args und **kwargs können eine beliebige anzahl parameter übergeben werden, die dann
                                #in args (tuple) respektive kwargs (dictionary) gespeichert sind.
                                #kann auch anders benennen, z.B. *meineparameter, entscheidend sind die
                                #UNPACKING OPERATOR * repsektive **

    print(request)
    print(args, kwargs)

    #return HttpResponse("<h1>Hello World</h1>")  # string of HTML code

    #ein Template (HTML-Dokument) übergeben, wenn view aufgerufen wird (über URL gelinkt)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [23435, 2345,4534, 'abc']
    }
    return render(request, "about.html", my_context)