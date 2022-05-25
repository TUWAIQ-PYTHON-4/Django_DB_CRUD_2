from django.db import models

# Create your models here.
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the Publisher.")
    website = models.URLField(help_text="The Publisher's website.")
    email = models.EmailField(help_text="The Publisher's email address.")


class Movies_Info(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the Movie.")
    date = models.DateField(verbose_name="Date the Movie was released.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="MovieContributor")


class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text="The contributor's first name.")
    last_name = models.CharField(max_length=50, help_text="The contributor's last name or name.")
    email = models.EmailField(help_text="The contact email for the contributor.")


class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was created.")
    movie = models.ForeignKey(Movies_Info, on_delete=models.CASCADE, help_text="The Movie that this review is for .")
