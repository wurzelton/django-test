from django import forms

from .models import Article

class BlogForm(forms.ModelForm): #a form especially for a created model

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]