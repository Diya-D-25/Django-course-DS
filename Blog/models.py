from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=100)
    Posted_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
