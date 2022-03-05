from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import (
    status,
    generics,
    authentication,
    permissions
)
from rest_framework.decorators import api_view
from .models import User
from .serializers import (
    UserSerializer, 
    UserRegistrationsSerializer,
    UserDepositSerializer,
    UserBuySerializer
)
from django.contrib.auth import logout
from product.models import Product
from .permissions import IsABuyer

class UserDeposit(APIView):
    permission_classes = [IsABuyer]
    serializer_class = UserDepositSerializer

    def post(self, request):
        serializer = UserDepositSerializer(data=request.data)
        user = User.objects.get(id=request.user.id)

        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            user.deposit += int(amount)
            user.save()
            serializer = UserSerializer(user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserReset(APIView):
    permission_classes = [IsABuyer]
    
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        user.deposit = 0
        user.save()
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserBuy(APIView):
    permission_classes = [IsABuyer]
    serializer_class = UserBuySerializer
    
    def post(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserBuySerializer(data={**request.data, 'user': request.user.id})
        if serializer.is_valid():
            user.deposit = serializer.data['balance']
            user.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationsSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationsSerializer(data=request.data)
        if serializer.is_valid():
            saved_user = serializer.save()
            serializer = UserSerializer(saved_user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'details': 'Missing authentication details'}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(data=request.data)

        if not request.user or not request.user.is_authenticated:
            return Response(data={'details': 'Missing authentication details'}, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            serializer.validated_data['id'] = user.id
            user = serializer.update(user, serializer.validated_data)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK )
        return Response({**serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(data=request.data)

        if not request.user or not request.user.is_authenticated:
            return Response(data={'details': 'Missing authentication details'}, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            serializer.validated_data['id'] = user.id
            user = serializer.update(user, serializer.validated_data)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK )
        return Response({**serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        