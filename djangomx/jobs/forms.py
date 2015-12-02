# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from django.forms import ModelForm

from .models import Job


class JobForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Job
        exclude = ('slug', 'created_at', 'updated_at', 'is_active', 'is_approved',)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 75:
            raise forms.ValidationError(_(u'El título no puede ser mayor a 75 caracteres.'))
        return title
