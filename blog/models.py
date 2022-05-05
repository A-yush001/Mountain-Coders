from pyexpat import model
from django.db import models
from numpy import True_

class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    content_dec=models.CharField(max_length=245,default='.....')
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    

    def __str__(self):
       return self.name