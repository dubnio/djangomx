# coding: utf-8
from django.test import TestCase
import factory
from .models import Job


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'jobs.Job'


class JobTestCase(TestCase):

    def test_big_slug(self):
        """
        Test for slug when job has a big title
        """
        big_title = "Duis mollis, est non commodo luctus, nisi erat porttitor \
        ligula, eget lacinia odio sem nec elit. Lorem ipsum dolor sit amet, \
        consectetur adipiscing elit."
        job = JobFactory.create(title=big_title)
        self.assertItemsEqual(job.title, big_title)
        self.assertIsNot(job, Job)
