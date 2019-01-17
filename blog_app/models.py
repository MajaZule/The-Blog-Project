from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length = 400)
    text = models.TextField()
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey('blog_app.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length = 200)
    text = models.CharField(max_length = 1000)
    published_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_list')
