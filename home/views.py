from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    peoples=[
        {'name': 'rehan', 'age': 24},
        {'name': 'ali', 'age': 4},
        {'name': 'subhan', 'age': 24},
        {'name': 'shahid', 'age': 24},
        {'name': 'rehan', 'age': 24},
        {'name': 'rehan', 'age': 2},
        {'name': 'azghar', 'age': 24},
        {'name': 'rehan', 'age': 24},
        {'name': 'imran', 'age': 2},
        {'name': 'rehan', 'age': 24},
    ]
    
    return render(request, "index.html", context={'page' : 'Home','peoples': peoples})

def about(request):
    context = {'page' : 'About'}
    return render(request, "about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html", context)


def success_page(request):
    print("*" * 11)
    return HttpResponse("<h1>Hey i am Rehan Khan is successfull programmer</h1>")
