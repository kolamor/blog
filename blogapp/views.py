from django.shortcuts import render
from django.views.generic import View
from blogapp.models import News, Category, Tag
# Create your views here.


class IndexPage(View):
	""" Index Html"""
	def get(self, request):
		news_list = News.objects.all()
		#tags = news_list.tag_set.all()

		context ={
				'news' : news_list,
				#'tags' : tags 
		}

		return render(request,'index.html', context)


class NewsView(View):

	def get(self, request, slug):
		
		return render(request, 'news_view.html')


