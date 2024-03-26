from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.ImageField(upload_to='static/news_images/')
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Game(models.Model):
    game = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='static/games_logo/', null=True, blank=True)

    def __str__(self):
        return self.game

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='static/tournaments_logo/')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    prize_pool = models.IntegerField()
    teams = models.ManyToManyField('Team', related_name='tournaments')

    def __str__(self):
        return f"{self.name} - ${self.prize_pool}"

class Team(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='static/teams_logo/')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    players = models.ManyToManyField('Player', through='TeamPlayer')

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team.name} - {self.player.name}"
