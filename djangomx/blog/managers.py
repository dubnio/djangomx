from django.db import models


class PostManager(models.Manager):
    def get_active(self):
        return super(PostManager, self).get_queryset().filter(is_active=True)
