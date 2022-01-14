from django.db import models


class External(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url_name = models.CharField(max_length=50)
    description = models.TextField()
    credit = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.name
