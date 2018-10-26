from django.contrib import admin
from blogapp.models import News, Category, Tag, Comments

from django_summernote.admin import SummernoteModelAdmin






class SlugAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title',) 

class NewsAdmin(SummernoteModelAdmin, SlugAdmin):
	summer_note_fields = ('text', 'text_min')

class SummernoteComments(SummernoteModelAdmin, admin.ModelAdmin):
	summer_note_fields = ('text',)
	list_display = ('user','news', 'date_create', 'moderation')



admin.site.register(News, NewsAdmin)
admin.site.register(Category, NewsAdmin)
admin.site.register(Tag, NewsAdmin)
admin.site.register(Comments, SummernoteComments)


