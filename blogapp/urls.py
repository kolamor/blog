from django.contrib import admin
from django.urls import path, include
from blogapp.views import IndexPage, NewsView



urlpatterns = [
    
    path('', IndexPage.as_view(), name='indexht'),
    path('<slug>/', NewsView.as_view(), name='news_view'),

]