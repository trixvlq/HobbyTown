from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    date_published = models.DateField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    video = models.URLField(max_length=255)

    def __str__(self):
        return self.title
