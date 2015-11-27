import datetime
from itertools import groupby

from django.test import (TestCase, RequestFactory)
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from model_mommy import mommy

from models import Post
from views import (archives, view_post)

class ProfileTestCase(TestCase):

    def setUp(self):
        # Create and client object
        self.factory = RequestFactory()
        # Create user 
        self.email = 'yo@dharwinperez.com'
        self.no_email = 'yo@dharwinperez.com'
        self.user = mommy.make(User, email=self.email) 
        
        # Create a post
        self.post = mommy.make(Post, author=self.user, slug="example")

    def test_archives(self):
    	
        request = self.factory.get(reverse('blog:archives'))

        response = archives(request)
        self.assertEqual(response.status_code, 200)

    def test_view_post(self):
        
        request = self.factory.get(reverse('blog:view_post',kwargs={'slug':self.post.slug}))

        response = view_post(request,self.post.slug)
        self.assertEqual(response.status_code, 200)