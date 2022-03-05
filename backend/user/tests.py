from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from backend.generators import *
from user.models import (
    User,
    UserRole,
    AllowedDeposit
)

CREATE_ENDPOINT = "/user/create/"
DEPOSIT_ENDPOINT = "/user/deposit/"
BUY_ENDPOINT = "/user/buy/"
PRODUCT_ENDPOINT = "/product/"

class UserTests(APITestCase, TestCase):

    def test_create_user_tp(self):
        """
        Ensure we can create user with valid details
        """

        user = random_user()
        response = self.client.post(CREATE_ENDPOINT, data=user, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_tn1(self):
        """
        Ensure we faill to create user when password do not match
        """

        user = random_user()
        user['password'] = random_string()
        response = self.client.post(CREATE_ENDPOINT, data=user, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username=user['username']).exists())

    def test_create_user_tn2(self):
        """
        Ensure we faill to create user when user role is not in choices
        """

        user = random_user()
        user['role'] = random_string()
        response = self.client.post(CREATE_ENDPOINT, data=user, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username=user['username']).exists())

class BuyerTests(APITestCase, TestCase):

    def setUp(self):
        self.user_1 = random_user()
        self.user_1['role'] = UserRole.BUYER.value
        response = self.client.post(CREATE_ENDPOINT, data=self.user_1, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.login(username=self.user_1['username'], password=self.user_1['password'])

    def test_buyer_deposit_tp(self):
        """
        Ensure buyer can deposit correct amounts
        """

        amount = random_choices(AllowedDeposit.values)
        data = {
            'amount': amount
        }

        response = self.client.post(DEPOSIT_ENDPOINT, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(username=self.user_1['username']).deposit, amount)

    def test_buyer_deposit_tn(self):
        """
        Ensure buyer cannot deposit incorrect amounts
        """

        amount = random_choices([0, 1, 2, 3, 4, 6, 7, 8])
        data = {
            'amount': amount
        }

        response = self.client.post(DEPOSIT_ENDPOINT, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_buyer_buy_tp(self):
        """
        Ensure buyer can buy product with enough balance
        """
        # create new seller user
        user_2 = random_user()
        user_2['role'] = UserRole.SELLER.value
        response = self.client.post(CREATE_ENDPOINT, data=user_2, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_2 = User.objects.get(username=user_2['username'])

        # Deposit enough funds into user account
        amount = 100
        data = {'amount': amount}
        response = self.client.post(DEPOSIT_ENDPOINT, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(username=self.user_1['username']).deposit, amount)

        product_1 = random_product()
        product_1['amountAvailable'] = 10 # ensure enough is available
        product_1['sellerId'] = user_2.id
        product_1['cost'] = 1 # set reasonable cost for text

        response = self.client.post(PRODUCT_ENDPOINT, data=product_1, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check user_1 can buy
        data = {
            "products": [
                {
                    "productId": 1,
                    "amount": 1,
                }
            ]
        }
        response = self.client.post(BUY_ENDPOINT, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_buyer_deposit_tn(self):
        """
        Ensure buyer cannot deposit incorrect amounts
        """

        amount = random_choices([0, 1, 2, 3, 4, 6, 7, 8])
        data = {
            'amount': amount
        }

        response = self.client.post(DEPOSIT_ENDPOINT, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_buyer_buy_fp_1(self):
        """
        Ensure buyer cannot buy product without enough balance
        """
        # create new seller user
        user_2 = random_user()
        user_2['role'] = UserRole.SELLER.value
        response = self.client.post(CREATE_ENDPOINT, data=user_2, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_2 = User.objects.get(username=user_2['username'])

        # Deposit not enough funds into user account
        amount = 5
        data = {'amount': amount}
        response = self.client.post(DEPOSIT_ENDPOINT, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(username=self.user_1['username']).deposit, amount)

        product_1 = random_product()
        product_1['amountAvailable'] = 10 # ensure enough is available
        product_1['sellerId'] = user_2.id
        product_1['cost'] = MAX_INT # set reasonable cost for text

        response = self.client.post(PRODUCT_ENDPOINT, data=product_1, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check user_1 can buy
        data = {
            "products": [
                {
                    "productId": 1,
                    "amount": 1,
                }
            ]
        }
        response = self.client.post(BUY_ENDPOINT, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
