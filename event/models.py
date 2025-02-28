from django.db import models
from django.utils import timezone
from pv_reunion.models import Cellule, Branch
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    cellule = models.ForeignKey(Cellule, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.CharField(max_length=200)
    description = models.TextField(default="No description provided" )
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def get_details(self):
        return f"Name: {self.name}, Date: {self.date}, Rating: {self.rating}"

    def update_rating(self, new_rating):
        self.rating = (self.rating + new_rating) / 2
        self.save()

    def __str__(self):
        return self.name