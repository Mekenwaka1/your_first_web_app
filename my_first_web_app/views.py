from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('home')

def gallery(request):
    return HttpResponseRedirect('portfolio')

def home_page(request):
    response = render(request, 'index.html')
    return HttpResponse(response)

def portfolio(request):
    response = render(request, 'portfolio.html')
    return HttpResponse(response)

def about_me(request):
    context = {'list_of_skills': ['coding', 'communication'], 'list_of_interests': ['reading', 'learning', 'speaking']} 
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def fave_links(request):
    context = {'google': "https://www.google.com/", 
    'wikipedia': "https://en.wikipedia.org/wiki/Main_Page", 
    'facebook': "https://www.facebook.com/"} 
    response = render(request, 'fave_links.html', context)
    return HttpResponse(response)

def images(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_url = "https://picsum.photos/400/600/?image={}".format(random_number)

    context = {'gallery_image': image_url}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)