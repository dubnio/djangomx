# coding: utf-8
from itertools import groupby

from django.contrib.syndication.views import Feed
from django.views.generic import ListView, DetailView

from .models import Category, Post


class BlogHomeView(ListView):
    model = Post
    queryset = Post.objects.get_active()
    paginate_by = 4
    template_name = 'blog_home.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.filter(post__in=self.get_queryset(), is_active=True),
        })
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class CategoryView(DetailView):
    model = Category
    queryset = Category.objects.filter(is_active=True)
    context_object_name = 'categories'
    paginate_by = 5
    template_name = 'category.html'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context.update({
            'posts': Post.objects.get_active().filter(category=self.object)
        })
        return context


class ArchivesView(ListView):
    model = Post
    queryset = Post.objects.get_active()
    template_name = 'archives.html'

    def get_context_data(self, **kwargs):
        context = super(ArchivesView, self).get_context_data(**kwargs)
        years = {
            k: list(g) for k, g in groupby(
                sorted(self.get_queryset(), key=lambda x: x.created_at.year),
                lambda x: x.created_at.year
            )
        }
        context.update({
            'archives': years,
        })
        return context


class LatestEntriesFeed(Feed):
    title = 'Django México'
    link = 'http://django.mx'
    description = 'La comunidad de Django en México'

    def items(self):
        return Post.objects.filter(is_active=True)[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_author_link(self, item):
        return item.author.profile.get_absolute_url()
