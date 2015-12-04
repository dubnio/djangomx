# coding: utf-8
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.db.models import TextField
from django.utils.translation import ugettext as _

from django_markdown.admin import AdminMarkdownWidget

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')


def disable_posts(modeladmin, request, queryset):
    queryset.update(is_active=False)

disable_posts.short_description = _("Disable Selected Post")


def available_posts(modeladmin, request, queryset):
    queryset.update(is_active=True)

available_posts.short_description = _("Available Selected Post")


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': AdminMarkdownWidget}
    }

    list_display = (
        'title', 'description', 'created_at', 'is_active', 'author'
    )

    actions = [disable_posts, available_posts]

    def has_obj_change_permission(self, obj, request):
        if obj.author == request.user or request.user.is_superuser:
            return True
        return False

    def save_form(self, request, form, change):
        obj = super(PostAdmin, self).save_form(request, form, change)
        if not change or self.has_obj_change_permission(obj, request):
            obj.author = request.user
        return obj

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(author=request.user)

    def render_change_form(self, request, context, *args, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ('author',)
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
