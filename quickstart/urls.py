from django.urls import path
from .views import CustomerCreate, CustomerList, CustomerDetail, CustomerUpdate, CustomerDelete


urlpatterns = [
    path('customer/create/', CustomerCreate.as_view(), name='create-customer'),
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'),
    path('customer/update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    path('customer/delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]
