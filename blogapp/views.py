from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from blogapp.models import News, Category, Tag, Comments
from blogapp.forms import CommentsForm
# Create your views here.


class IndexPage(View):
	""" Index Html"""
	def get(self, request):
		news_list = News.objects.all()
		

		context ={
				'news' : news_list,
				 
		}

		return render(request,'index.html', context)


class NewsView(View):

	def get(self, request, slug):

		news_full = News.objects.get(slug__iexact=slug)

		comments = Comments.objects.filter(news=news_full.id, moderation=True)
		form = CommentsForm()

		context ={
				'news_full' : news_full,
				'comments'  : comments,
				'form'      : form,
		}
			
		return render(request, 'news_view.html', context)


	def post(self, request, slug):

		news_full = News.objects.get(slug__iexact=slug)

		form = CommentsForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.news = news_full
			form.save()

		return redirect('news_view', slug )
		



