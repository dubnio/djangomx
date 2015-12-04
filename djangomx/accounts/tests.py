from django.contrib.auth.models import User
from django.test import TestCase

from django_gravatar.helpers import has_gravatar
from model_mommy import mommy

from blog.models import Post
from .models import Profile


class ProfileTestCase(TestCase):

    def setUp(self):
        self.email = 'me@netoxico.com'
        self.no_email = 'no@netoxico.com'
        self.user = mommy.make(User, email=self.email)

    def test_avatar(self):
        profile = mommy.make(Profile, user=self.user)

        self.assertTrue(has_gravatar(self.email))
        self.assertFalse(has_gravatar(self.no_email))
        self.assertFalse(profile.avatar)

        profile.avatar = profile.user.email

        self.assertTrue(profile.avatar)

    def test_create_from_user(self):
        profile = Profile.create_from_user(self.user)

        self.assertEqual(profile.user, self.user)
        self.assertEqual(Profile.objects.all().count(), 1)


class ProfileViewTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make(User, username='test', email='me@netoxico.com')
        self.profile = mommy.make(Profile, user=self.user)
        self.post1 = mommy.make(Post, author=self.user)
        self.post2 = mommy.make(Post, author=self.user)
        self.post3 = mommy.make(Post, author=self.user)
        self.post4 = mommy.make(Post, author=self.user, is_active=False)

    def test_get_profile(self):
        response = self.client.get(self.profile.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/profile.html')

    def test_get_context_data(self):
        response = self.client.get(self.profile.get_absolute_url())
        context = response.context
        posts = self.profile.user.post.get_active()
        self.assertEqual(context['posts'].count(), posts.count())
