from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from product.models import Product

class Cart(models.Model):
    userId = models.ForeignKey(User,on_delete= models.CASCADE)
    product = models.ForeignKey(Product ,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=20, blank= False)
    color = models.CharField(max_length=20, blank= False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return '{}/{}'.format(self.userId.username,self.product.title)
