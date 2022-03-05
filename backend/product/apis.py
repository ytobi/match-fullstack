from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly
from .serializer import ProductSerializer


class ProductCreateOrList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['sellerId'] = request.user
            product = serializer.save()
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response({**serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PeroductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PeroductUserList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        userProducts = Product.objects.filter(sellerId=request.user.id)
        serializer = ProductSerializer(userProducts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
