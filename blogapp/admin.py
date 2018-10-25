from django.contrib import admin
from blogapp.models import News, Category, Tag

from django_summernote.admin import SummernoteModelAdmin






class SlugAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title',) 

class NewsAdmin(SummernoteModelAdmin, SlugAdmin):
	summer_note_fields = ('text', 'text_min')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, NewsAdmin)
admin.site.register(Tag, NewsAdmin)
