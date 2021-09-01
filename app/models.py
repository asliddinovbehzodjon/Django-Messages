from django.db import models

# Create your models here.
class Example(models.Model):
    item=models.CharField(max_length=350)
    def __str__(self):
        return self.item
    