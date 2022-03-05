import random
import string
import math
from django.utils import timezone
from user.models import UserRole

EXAMPLE_DOMAIN = "example.com"
DEFAULT_STRING_LEGNTH = 10
DEFAULT_PHONE_LEGNTH = 9
MAX_INT = 2147483647
MIN_INT = -MAX_INT+1
MAX_BIGINT = 9223372036854775807
MIN_BIGINT = -MAX_BIGINT+1


def random_string(length=DEFAULT_STRING_LEGNTH, letters=string.ascii_letters):
    return "".join(random.choice(letters) for i in range(0, length))


def random_interger(minimum=MIN_INT, maximum=MAX_INT):
    return random.randint(minimum, maximum)


def random_bool():
    return bool(random.randint(0, 1))


def random_choices(choices):
    return choices[random_interger(0, len(choices)-1)]


def random_date():
    return timezone.now()


def random_user(length=DEFAULT_STRING_LEGNTH, letters=string.ascii_letters):
    username = random_string(length=DEFAULT_STRING_LEGNTH, letters=string.ascii_letters)
    password = random_string(length=DEFAULT_STRING_LEGNTH, letters=string.ascii_letters)
    password2 = password
    role = random_choices(UserRole.values)
    data = {
        'username': username,
        'password': password,
        'password2': password2,
        'role': role,
    } 
    return data


def random_product(length=DEFAULT_STRING_LEGNTH, letters=string.ascii_letters):
    amountAvailable = random_interger(0)
    cost = random_interger(0)
    productName = random_string()
    sellerId = random_interger(0)
    data = {
        'amountAvailable': amountAvailable,
        'cost': cost,
        'productName': productName,
        'sellerId': sellerId,
    } 

    return data
