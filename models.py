from django.db import models

# Create your models here.
#pass-- Root@123

class APIAPP(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name