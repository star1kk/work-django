from django import forms
from .models import Article

active_fields = [
    'title', 'description'
]


class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = active_fields
