from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.ImageField(upload_to='static/news_images/')
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title