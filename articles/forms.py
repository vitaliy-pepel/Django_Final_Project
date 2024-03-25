from django import forms
from .models import Author, Article, Comment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'biography', 'birth_date']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'category', 'is_published']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'article', 'comment']
