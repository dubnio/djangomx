# coding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)

    def has_obj_change_permission(self, obj, request):
        if obj.author == request.user or request.user.is_superuser:
            return True
        return False

    def save_form(self, request, form, change):
        obj = super(ProfileAdmin, self).save_form(request, form, change)
        if not change:
            obj.user = request.user
        return obj

    def get_queryset(self, request):
        qs = super(ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
