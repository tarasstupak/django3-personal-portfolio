from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    date = models.DateField()

    def __str__(self):
        return self.title