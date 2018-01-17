from django.db import models

# Create your models here.
class URLDB(models.Model):
    Num = models.IntegerField()
    Name =models.CharField(max_length=100)
    URL =models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    def __str__(self):
        return self.Time


class TabName(models.Model):
    Num = models.IntegerField()
    TabName = models.CharField(max_length=100)
