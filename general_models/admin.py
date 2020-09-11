from django.contrib import admin

from .models import GeneralModel


class GeneralModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'genre', 'owner', 'frontpage_feature_slot', 'is_published', 'category_feature_slot', 'tags')
    list_display_links = ('title',)
    list_filter = ('owner',)
    list_editable = ('is_published', 'frontpage_feature_slot', 'category_feature_slot')
    search_fields = ('title', 'content', 'author')
    list_per_page = 10

admin.site.register(GeneralModel, GeneralModelAdmin)
