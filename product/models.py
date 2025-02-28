from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255,unique=True)
    imageUrl = models.URLField(blank=False)
    def __str__(self) -> str:
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=255,unique=True)
    price = models.FloatField(default=0,blank=False)
    description = models.TextField(max_length=500)
    productType = models.CharField(max_length=255,default='standard')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    ratings = models.FloatField(blank= False,default=1.0)
    colors = models.JSONField(blank=True)
    sizes = models.JSONField(blank=True)
    imageUrls = models.JSONField(blank= True)
    created_at = models.DateTimeField(default=timezone.now,blank= False)
    
    def __str__(self) -> str:
        return self.title


