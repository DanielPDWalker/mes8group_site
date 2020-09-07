from django.contrib import admin

from .models import WritingModel


class WritingModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'genre', 'owner', 'feature_slot', 'is_published', 'tags')
    list_display_links = ('title',)
    list_filter = ('owner',)
    list_editable = ('is_published', 'feature_slot')
    search_fields = ('title', 'content', 'author')
    list_per_page = 10

admin.site.register(WritingModel, WritingModelAdmin)
