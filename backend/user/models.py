from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserRole(models.TextChoices):
    BUYER = 'Buyer', 'Buyer'
    SELLER = 'Seller', 'Seller'

class AllowedDeposit(models.IntegerChoices):
    FIVE = 5
    TEN = 10
    TWENTY = 20
    FIFTY = 50
    HUNDRED = 100

class User(AbstractUser):
    deposit = models.IntegerField(default=0)
    role = models.CharField(
        choices=UserRole.choices, 
        null=False, 
        max_length=225, 
        help_text= "Role must be one of " + str(UserRole.values),
    )