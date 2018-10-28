from django.contrib import admin
from django.urls import path, include
from blogapp.views import IndexPage, NewsView, ProfileUser, InputNews



urlpatterns = [
    
    path('', IndexPage.as_view(), name='indexht'),
    path('<slug>/', NewsView.as_view(), name='news_view'),
    path('profile/<user>/', ProfileUser.as_view(), name='profile_user'),
    path('inputnews/add/', InputNews.as_view(), name='input_news'),

]