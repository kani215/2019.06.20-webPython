from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reservation/', views.movieSelect),
    path('movieIssue/', views.movieIssue),
    path('myhistory/', views.myhistory),
]
