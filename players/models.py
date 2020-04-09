from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=40)
    club_state = models.CharField(max_length=50)

    def __str__(self):
        return self.club_state


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player')
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    jersey_number = models.IntegerField()
    country = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name
