from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Author, Article, Comment
from .forms import AuthorForm, ArticleForm, CommentForm


def index(request):
    authors = Author.objects.all()
    articles = Article.objects.all()

    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        article_form = ArticleForm(request.POST)
        comment_form = CommentForm(request.POST)

        if 'create_author' in request.POST:
            if author_form.is_valid():
                author_form.save()
                return redirect('articles:index')

        elif 'create_article' in request.POST:
            if article_form.is_valid():
                article_form.save()
                return redirect('articles:index')

        elif 'create_comment' in request.POST:
            if comment_form.is_valid():
                comment_form.save()
                return redirect('articles:index')

    else:
        author_form = AuthorForm()
        article_form = ArticleForm()
        comment_form = CommentForm()

    context = {
        'authors': authors,
        'articles': articles,
        'author_form': author_form,
        'article_form': article_form,
        'comment_form': comment_form,
    }

    return render(request, 'articles/index.html', context)
