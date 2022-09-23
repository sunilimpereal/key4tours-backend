from email.mime import image
from pyexpat import model
from django.db import models

# Create your models here.


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True)
    show_on_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Visa(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    documents_required = models.TextField(max_length=1500)
    description = models.TextField(max_length=500, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(
        upload_to="visaThumbnails", height_field=None, width_field=None, max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name


class VisaCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True)
    price = models.IntegerField(max_length=10)
    visa = models.ForeignKey(Visa, on_delete=models.CASCADE)

    def __str__(self):
        return self.visa.name + ' ' + self.name
