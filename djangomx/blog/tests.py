from django.contrib.auth.models import User
from django.http import Http404
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from model_mommy import mommy

from .models import Post, Category
from . import views


class CategoryTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title='Testing')

    def test_url(self):
        url = '/blog/categoria/{category}/'.format(category=self.category.slug)
        dynamic_url = self.category.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(url, dynamic_url)
        self.assertEqual(response.status_code, 200)


class BlogViewsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = mommy.make(User, email='me@netoxico.com')
        self.post = mommy.make(Post, author=self.user, title='Test title')

    def get_blog_home(self):
        request = self.factory.get(reverse('blog:blog_home'))
        response = views.BlogHomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='blog_home.html')

    def test_get_archives(self):
        response = self.client.get(reverse('blog:archives'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='archives.html')


class PostTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make(User, email='me@netoxico.com')
        self.post = mommy.make(Post, author=self.user, title='Test title')

    def test_get_post(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='post.html')

    def test_post_url(self):
        url = '/blog/{year}/{month}/{day}/{slug}/'.format(
            year=self.post.created_at.year,
            month=self.post.created_at.month,
            day=self.post.created_at.day,
            slug=self.post.slug,
        )
        response = self.client.get(url)
        dynamic_url = self.post.get_absolute_url()

        self.assertEqual(url, dynamic_url)
        self.assertEqual(response.status_code, 200)

    def test_outdated_post_url(self):
        url = '/blog/{slug}/'.format(slug=self.post.slug)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.post.get_absolute_url())

    def test_wrong_url(self):
        url = '/blog/not-valid-url/'
        with self.assertRaises(Http404):
            self.client.get(url)
