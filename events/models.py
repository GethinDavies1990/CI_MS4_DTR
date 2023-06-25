from django.db import models
from datetime import datetime
info/templates/meet_the_team.html

SERVICE_CHOICES = (
    ("Fajita Party", "Fajita Party"),
    ("Taco Party", "Taco Party"),
    ("Taco y Tequila Special", "Taco y Tequila Special"),
    )
TIME_CHOICES = (
    ("2 PM", "2 PM"),
    ("5.30 PM", "5.30 PM"),
)

class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Fajita Party")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="5.30 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
