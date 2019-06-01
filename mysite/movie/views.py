from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie


def index(request):
    return render(request, 'movie/index.html')


def movieSelect(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movie/reservation/movieSelect.html', context)


def movieIssue(request):
    return render(request, 'movie/movieIssue.html')


def myhistory(request):
    return render(request, 'movie/myhistory.html')