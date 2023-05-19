from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    message = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name


