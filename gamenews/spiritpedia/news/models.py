from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.ImageField(upload_to='static/news_images/')
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Tournament(models.Model):
  """Модель турнира."""
  image = models.ImageField(upload_to='tournaments')
  name = models.CharField(max_length=255)
  organizer = models.CharField(max_length=255)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  teams = models.ManyToManyField('Team')

  def __str__(self):
    return self.name
  
class Team(models.Model):
  """Модель команды."""
  logo = models.ImageField(upload_to='teams')
  name = models.CharField(max_length=255)
  players = models.TextField()

  def __str__(self):
    return self.name