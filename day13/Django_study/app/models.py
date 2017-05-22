from django.db import models

# Create your models here.

class Host(models.Model):
    HostName = models.CharField(max_length=256)
    Ip = models.IPAddressField()
    CreateDate = models.DateTimeField(auto_now = True)
