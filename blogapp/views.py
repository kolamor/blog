from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from blogapp.models import News, Category, Tag, Comments
from blogapp.forms import CommentsForm
from django.core.paginator import Paginator

# Create your views here.


def news_paginator(paginator, page_number):
	
	# paginator = Paginator(products,4)		
	# page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginator = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''
	return (page, prev_url, next_url)


class IndexPage(View):
	""" Index Html"""
	def get(self, request):
		news_list = News.objects.all()
		paginator = Paginator(news_list,2)
		page_number = request.GET.get('page', 1)
		page, prev_url, next_url = news_paginator(paginator, page_number)

		

		context ={
				'news' : news_list,
				'page_object': page,
		        'next_url'   : next_url,
		        'prev_url'   : prev_url,
				 
		}

		return render(request,'index.html', context)


class NewsView(View):

	def get(self, request, slug):

		news_full = News.objects.get(slug__iexact=slug)

		comments = Comments.objects.filter(news=news_full.id, moderation=True)
		paginator = Paginator(comments, 2)
		page_number = request.GET.get('page', 1)
		page, prev_url, next_url = news_paginator(paginator, page_number)
		form = CommentsForm()

		context ={
				'news_full' : news_full,
				'comments'  : comments,
				'form'      : form,
				'page_object': page,
		        'next_url'   : next_url,
		        'prev_url'   : prev_url,
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
		



