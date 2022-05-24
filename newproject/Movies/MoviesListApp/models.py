from django.db import models

class Bee_hive(models.Model):
    gid = models.IntegerField(primary_key=True)
    hive_title = models.CharField(max_length=50)
    date_hive_death = models.DateField()
    date_hive_created = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.hive_title