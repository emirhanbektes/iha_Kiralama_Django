from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    user = models.IntegerField()
    startdate = models.DateField()
    stopdate = models.DateField()
    product = models.IntegerField()

    def clean(self):
        if self.stopdate <= self.startdate:
            raise ValidationError('Stop date must be after start date.')
        super().clean()

    def __str__(self):
        return f"User ID: {self.user} - Product ID: {self.product}"