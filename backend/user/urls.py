from django.urls import path
from . import apis

urlpatterns = [
    path('create/', apis.UserCreate.as_view()),
    path('', apis.UserDetails.as_view()),
    path('deposit/', apis.UserDeposit.as_view()),
    path('buy/', apis.UserBuy.as_view()),
    path('reset/', apis.UserReset.as_view()),
]
