from django.db import models
from django.core.validators import MinValueValidator
from user.models import User
# Create your models here.

class Product(models.Model):
    amountAvailable = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    cost = models.DecimalField(null=False, decimal_places=2, max_digits=12)
    productName = models.CharField(null=False, max_length=255)
    sellerId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)