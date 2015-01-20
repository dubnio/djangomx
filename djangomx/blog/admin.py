# coding: utf-8
from django.contrib import admin
from django.forms import ModelForm
from blog.models import Category, Post

from suit_redactor.widgets import RedactorWidget


class PageForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'extract': RedactorWidget(editor_options={'lang': 'es'}),
            'content': RedactorWidget(editor_options={'lang': 'es'})
        }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'created_at', 'is_active')


class PostAdmin(admin.ModelAdmin):
    form = PageForm
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'created_at', 'is_active')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
