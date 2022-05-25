from django.db import models

# Create your models here.

class AboutModel(models.Model):
    # fields of the model
    name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)

    # renames the instances of the model
    # with their name
    def __str__(self):
        return self.name