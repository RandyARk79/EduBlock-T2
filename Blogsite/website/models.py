from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    '''on user delete the post get deleted'''
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=1050)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    data_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " | " + str(self.author)


