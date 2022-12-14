from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article
from .forms import NewArticle

active_fields = [
    'title', 'description'
]


class ArticleListView(ListView):
    model = Article
    template_name = 'blog_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog_detail.html'


class ArticleCreateView(CreateView):
    form_class = NewArticle
    template_name = 'blog_new.html'
    success_url = reverse_lazy('blog_list')



class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'blog_edit.html'
    fields = active_fields
    success_url = reverse_lazy('blog_list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')
