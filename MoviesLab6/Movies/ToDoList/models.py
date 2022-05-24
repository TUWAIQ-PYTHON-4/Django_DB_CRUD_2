from django.db import models

class PublisherList(models.Model):
    name= models.CharField(max_length=50, help_text="Name of list")
    website= models.URLField(max_length=100, help_text='URL of list')
    email= models.EmailField(help_text='Email for the list')

    def __str__(self):
        return self.name
