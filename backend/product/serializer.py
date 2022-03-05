from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        extra_kwargs = {'sellerId': {'read_only': True}}
        fields = '__all__'


class ProductBuySerializer(serializers.Serializer):
    productId = serializers.IntegerField(required=True)
    amount = serializers.IntegerField(required=True)
    class Meta:
        fields = ['productId', 'amount']
    
    def validate(self, data):
        productId = data['productId']
        amount = data['amount']

        # validate product exist
        if not Product.objects.filter(id=productId).exists():
            raise serializers.ValidationError('Product does not exits')
        # validate if there are enough products to buy
        if Product.objects.get(id=productId).amountAvailable < int(amount):
            raise serializers.ValidationError('Not enough product to purchace')   
        return data