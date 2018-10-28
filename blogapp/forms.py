from django.forms import ModelForm
from django import forms
from .models import Comments, News
#from django.contrib import admin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SomeForm(forms.Form):
    text = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
    text_min = forms.CharField(widget=SummernoteWidget())


class AnotherForm(forms.Form):
   
    text = forms.CharField(widget=SummernoteInplaceWidget())
    text_min = forms.CharField(widget=SummernoteInplaceWidget())



class CommentsForm(ModelForm):
	

	class Meta:
		model = Comments
		fields = ('text',)


class NewsForm(SomeForm, forms.ModelForm):
	


	class Meta:

		model = News
		fields = ['title', 'slug', 'category', 'tags','text','text_min','description','image']
		
		widget = {
		    'title' : forms.TextInput(attrs={'class': 'form-control'}),
		    'slug' : forms.TextInput(attrs={'class': 'form-control'}),
		    'category' : forms.TextInput(attrs={'class': 'form-control'}),
		    'tags' : forms.TextInput(attrs={'class': 'form-control'}),
		    'text' : SummernoteInplaceWidget(),
		    'text_min' : SummernoteInplaceWidget(),
		    'description' : forms.TextInput(attrs={'class': 'form-control'}),
		    'image': forms.FileInput(attrs={'class': 'form-control'}),


		    
		    }