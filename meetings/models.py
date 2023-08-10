from django.db import models
from datetime import time
# Create your models here.


# Create a Model class called Room
# To represent a meeting room
# A room has a name, a floor number, and a room number


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor_number}"


class Meeting(models.Model):
    # Meeting class has a title and a date - after creating these attributes, we should be able to store that data from this model in our database.
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))  # meeting start_time
    duration = models.IntegerField(default=1)  # meeting duration in hours
    # This will hold the ID of the room object that this meeting references - allows us to select a room when we create a meeting
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

# In order to create a table for meetings, on terminal, write:
# => python3 manage.py makemigrations


# This methods returns a string with the title, start_time, and the meeting date


    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
