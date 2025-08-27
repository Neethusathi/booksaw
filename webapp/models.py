from django.db import models

# Create your models here.
class userDB(models.Model):
    uname=models.CharField(max_length=50,null=True,blank=True)
    u_password=models.CharField(max_length=50,null=True,blank=True)
    c_password=models.CharField(max_length=50,null=True,blank=True)
    email_address=models.CharField(max_length=50,null=True,blank=True)
class cartDB(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    productname = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField( null=True, blank=True)
    price = models.IntegerField( null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)
    prod_img = models.ImageField(upload_to="cart_image",  null=True, blank=True)
class checkoutDB(models.Model):
    firstname = models.CharField(max_length=100,null=True,blank=True)
    lastname = models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField( null=True, blank=True)
    pin =models.IntegerField( null=True, blank=True)
    Totalprice =models.IntegerField( null=True, blank=True)