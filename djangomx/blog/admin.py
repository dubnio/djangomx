# coding: utf-8
from django.contrib import admin
from django.forms import ModelForm
from django.db.models import TextField
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _

from suit_redactor.widgets import RedactorWidget

from django_markdown.admin import AdminMarkdownWidget

from blog.models import Category, Post

class PageForm(ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'slug',
            'image',
            'content',
            'extract',
            'category',
            'published_at',
            'author',
            'likes',
            'is_active'
        )
        widgets = {
            'content': RedactorWidget(
                editor_options={'lang': 'es', 'minHeight': 400}
            ),
            'extract': RedactorWidget(
                editor_options={'lang': 'es', 'minHeight': 200}
            )
        }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'created_at', 'is_active')

def disable_posts(modeladmin, request, queryset):
    queryset.update(is_active=False)
disable_posts.short_description = _("Disable Selected Post")

def available_posts(modeladmin, request, queryset):
    queryset.update(is_active=True)
available_posts.short_description = _("Available Selected Post")

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {
            'widget': AdminMarkdownWidget
        }
    }

    prepopulated_fields = {'slug': ('title', )}
    list_display = (
        'title',
        'slug',
        'description',
        'created_at',
        'is_active',
        'author'
    )
    actions = [disable_posts, available_posts]

    def has_obj_change_permission(self, obj, request):
        if obj.author == request.user or request.user.is_superuser:
            return True
        else:
            return False

    def save_form(self, request, form, change):
        obj = super(PostAdmin, self).save_form(request, form, change)
        if not change:
            obj.author = request.user
        if self.has_obj_change_permission(obj, request):
            obj.author = request.user
        return obj

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(author=request.user)

    def render_change_form(self, request, context, *args, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ('author',)
        else:
            self.exclude = None
        obj = context.get('original')
        if not obj:
            return super(PostAdmin, self).render_change_form(
                request, context, args, kwargs
            )
        if obj and self.has_obj_change_permission(obj, request):
            return super(PostAdmin, self).render_change_form(
                request, context, args, kwargs
            )
        else:
            raise PermissionDenied()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
