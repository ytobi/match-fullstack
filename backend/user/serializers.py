from rest_framework import serializers
from .models import (
    User,
    AllowedDeposit,
)
from product.models import Product
from product.serializer import ProductBuySerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = [
            'id',
            'username',
            'deposit',
            'role',
            'password',
        ]
        read_only_fields = ['id', 'deposit']
        extra_kwargs = {'username': {'required': False}, 'role': {'required': False}, 'password': {'required': False}}

class UserRegistrationsSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = [
            'id',
            'username',
            'deposit',
            'role',
            'password',
            'password2'
        ]
        read_only_fields = ['id']

    def save(self, **kwargs):
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']
        deposit = self.validated_data.get('deposit', 0)

        if password1 != password2:
            raise serializers.ValidationError(
                {'password': 'Password must match'}
            )
        
        del self.validated_data['password2']
        self.validated_data['deposit'] = deposit
        user = User.objects.create_user(**self.validated_data)
        return user


class UserDepositSerializer(serializers.Serializer):
    amount = serializers.ChoiceField(choices=AllowedDeposit.values, required=True)

    class Meta:
        fields = ['amount']

class UserBuySerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)
    products = ProductBuySerializer(required=True, many=True)
    totalAmountSpent = serializers.SerializerMethodField(
            'cal_totalAmountSpent')
    balance = serializers.SerializerMethodField('cal_balance')

    def validate(self, data):
        products_to_buy = ProductBuySerializer(data=data['products'], many=True)
        if not products_to_buy.is_valid():
            raise serializers.ValidationError(products_to_buy.errors)
        # Validate if user has enough balance to pay
        if self.cal_totalAmountSpent(data) >= self.cal_balance(data):
            raise serializers.ValidationError("You don't have enough balance to purchase")
        return data

    class Meta:
        fields = [
            'user',
            'products',
            'totalAmountSpent',
            'balance'
        ]
        extra_kwargs = {
            'totalAmountSpent': { 'read_only': True },
            'balance': { 'read_only': True },
            }

    def cal_totalAmountSpent(self, data):
        total_amount = 0
        for prd in data['products']:
            product = Product.objects.get(id=prd['productId'])
            total_amount +=  product.cost * int(prd['amount'])
        return total_amount

    def cal_balance(self, data):
        user = User.objects.get(id=data['user'])
        return user.deposit - self.cal_totalAmountSpent(data)

    def save(self, **kwargs):
        pass
