from django.db import models
from django.contrib.auth.models import User


class Pixel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    color = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.x}, {self.y} --> {self.color}'
