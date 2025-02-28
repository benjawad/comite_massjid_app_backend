from django.db import models

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='branch_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Cellule(models.Model):
    id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cellule_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PVReunion(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    cellule = models.ForeignKey(Cellule, on_delete=models.CASCADE)
    content = models.FileField(upload_to='pdfs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
