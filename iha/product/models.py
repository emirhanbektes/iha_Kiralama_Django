from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class category (models.Model):
    name = models.CharField(max_length=100)
    aciklama = models.TextField()
    
    def __str__(self):
        return f"{self.name}"
    
class Product (models.Model): 
    title = models.CharField(max_length=50) 
    description = models.TextField() 
    imageUrl = models.CharField(max_length=50, blank=False) 
    date= models.DateField()  
    weight = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        blank=True,
        null=True,
    )
    slug= models.SlugField (default="", blank=True, editable=False, null=False, unique=True, db_index=True)       
    category = models.ForeignKey(category, on_delete=models.CASCADE) 

    def save(self, *args, **kwargs):         
        self.slug= slugify(self.title)
        super().save(args, kwargs)        
        
        def __str__(self):
            return f"{self.name}"
        


