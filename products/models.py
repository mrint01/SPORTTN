from django.db import models
from ckeditor.fields import RichTextField
from django.utils import safestring
from django.utils.safestring import SafeString, mark_safe

# Create your models here.


class Product(models.Model):
    nameP = models.CharField(max_length=100)
    descP = RichTextField()
    imageP = models.ImageField(upload_to="./products/images/")
    prixP=  models.IntegerField()

    def image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.imageP.url))

    def __str__(self):
        return self.nameP

class Proteines(Product):

    def __str__(self):
        return self.nameP

class Materiels(Product):

    Materiels_Choises =(
        ('Fitness' ,'Fitness'),
        ('BodyBuilding','BodyBuilding')
    )
    typeM = models.CharField(max_length=100 , choices=Materiels_Choises)

    def __str__(self):
        return self.typeM

class Vetements(Product):
    Vetements_Choises =(
        ('Femme','Femme'),
        ('Homme','Homme')
    )
    genre = models.CharField(max_length=100 , choices=Vetements_Choises)

    def __str__(self):
        return self.genre
