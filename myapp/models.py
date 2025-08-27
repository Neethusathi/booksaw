from django.db import models

class categoryDB(models.Model):
    catename=models.CharField(max_length=50,blank=True,null=True)
    cimage=models.ImageField(upload_to="category_file",blank=True,null=True)
    description=models.CharField(max_length=50,blank=True,null=True)

class productDB(models.Model):
    select_pro=models.CharField(max_length=50,null=True,blank=True)
    proname=models.CharField(max_length=50,null=True,blank=True)
    proimg=models.ImageField(upload_to="product_image" ,null=True,blank=True)
    cost=models.IntegerField(null=True,blank=True)
    pdesc=models.CharField(max_length=50,null=True,blank=True)
