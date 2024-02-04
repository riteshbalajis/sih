from django.db import models

# Create your models here.
class storelogin(models.Model):
    shopname = models.CharField(max_length=250)
    shopno = models.CharField(max_length=100,default='')
    address = models.TextField(max_length=1000,default='')
    city = models.CharField(max_length=250,default='')
    district = models.CharField(max_length=250,default='')
    pincode = models.CharField(max_length=10,default='')
    contact = models.CharField(max_length=10,default='')
    ownerfirstname = models.CharField(max_length=250)
    ownersecondname = models.CharField(max_length=250)
    ownerusername = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    ownerpassword = models.CharField(max_length=250)
    confirmpass = models.CharField(max_length=250)