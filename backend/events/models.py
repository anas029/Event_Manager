from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='events_participating', blank=True)

    def __str__(self):
        return self.title
