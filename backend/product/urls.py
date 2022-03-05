from django.urls import path
from . import apis

urlpatterns = [
    path('', apis.ProductCreateOrList.as_view()),
    path('<int:pk>/', apis.PeroductDetails.as_view()),
    path('user/', apis.PeroductUserList.as_view()),
]
