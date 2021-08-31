from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to="images/", default="wp2027011.jpg")

    def __str__(self):
        return self.title
