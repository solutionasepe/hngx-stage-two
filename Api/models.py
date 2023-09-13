from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name