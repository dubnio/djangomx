from django.contrib.auth.models import User
from django.test import TestCase

from django_gravatar.helpers import has_gravatar
from model_mommy import mommy

from .admin import ProfileAdmin
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


class ProfileAdminTestCase(TestCase):

    def setUp(self):
        self.user1 = mommy.make(User)
        self.user2 = mommy.make(User)
        self.user3 = mommy.make(User)
        self.profile1 = mommy.make(Profile, user=user1)
        self.profile2 = mommy.make(Profile, user=user2)
        self.profile3 = mommy.make(Profile, user=user3)

    def test_blogpost_pending(self, obj):
        blogpost_pending = Profile.blogpost_pending()
