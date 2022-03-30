from django.shortcuts import render
from django.http import HttpResponse

def news_view(request):
    return render(request,"demoapp/home.html")

def movie_view(request):
    news1="Hit movies"
    news2="Flop movies"
    my_dict={'N1':news1,'N2':news2}
    return render(request,"demoapp/movie.html",my_dict)

def politics_view(request):
    news1="Good Politics"
    news2="Dirty Politics"
    my_dict={'N1':news1,'N2':news2}
    return render(request,"demoapp/politics.html",my_dict)

def sports_view(request):
    news1="Fair Sports"
    news2="Unfair Sports"
    my_dict={'N1':news1,'N2':news2}
    return render(request,"demoapp/sports.html",my_dict)
