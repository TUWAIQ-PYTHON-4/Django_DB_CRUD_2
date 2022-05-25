from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, help_text="publisher name")
    email = models.EmailField(help_text="email of publisher")
    website = models.URLField(help_text="publisher website")

    def __str__(self):
        return self.name
