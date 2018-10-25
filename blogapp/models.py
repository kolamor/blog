from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
User = get_user_model()


def  generate_filename(instance, filename):
	 filename = instance.slug +'.'+ filename.split('.')[1]
	 return "{0}/{1}".format(instance, filename)


class Category(models.Model):
	""" Category model"""
	title = models.CharField('название', max_length=30)
	slug = models.SlugField('slug', max_length=30, unique=True)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


	def __str__(self):
		return self.title


class Tag(models.Model):
	""" Tag model"""
	title = models.CharField('название', max_length=30)
	slug = models.SlugField('slug', max_length=30, unique=True)


	class Meta:
		verbose_name = 'Тег'
		verbose_name_plural = 'Теги'


	def __str__(self):
		return self.title

class News(models.Model):
	"""Статьи model"""
	title = models.CharField('название', max_length=50)
	slug = models.SlugField('slug', max_length=50, unique=True)
	user = models.ForeignKey(
					User,
					verbose_name='Автор',
					on_delete=models.SET_NULL,
					null=True)
	category = models.ForeignKey(
					Category,
					verbose_name='категория',
					on_delete=models.SET_NULL,
					null=True)

	tags = models.ManyToManyField(
					Tag,
					verbose_name='Теги')
					
	text = models.TextField('Текст статьи')
	text_min = models.TextField('Текст статьи', max_length=300)
	date_created = models.DateTimeField('Дата создания', auto_now_add=True)
	description = models.CharField('Описание', max_length=100)
	like = models.IntegerField('Лайки')
	image = models.ImageField(upload_to=generate_filename, blank=True)


	
	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'
		ordering = ['date_created']



	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('news_view', kwargs={'slug' : self.slug})








