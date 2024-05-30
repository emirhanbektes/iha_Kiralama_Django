from django.urls import path
from userview.views import customer_rent, update_rent_date,userRent_list,delete_user_profile

urlpatterns = [

    path('customer_rent/', customer_rent, name='customer_rent'),
    path('update_rent_date/<int:pk>/', update_rent_date, name='update_rent_date'), 
    path('list/', userRent_list, name='userRent_list'),
    path('delete_profile/<int:pk>/', delete_user_profile, name='delete_user_profile'),

]