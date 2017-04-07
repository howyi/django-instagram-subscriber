from django.db import models

class Media(models.Model):
    date = models.DateTimeField('date published', null=True)
    data = models.CharField(max_length=2000, null=True)
