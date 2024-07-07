from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    description = models.TextField()

    def __str__(self):
        return self.name