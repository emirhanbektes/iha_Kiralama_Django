from django.urls import path
from product.views import  add_product, updateProduct,add_category,update_Product,product_list,deleteProduct,rent,rent_product
urlpatterns = [

    path('updateProduct/', updateProduct, name='updateProduct'),
    path('rent/', rent, name='rent'),
    path('add_product/', add_product, name='add_product'),
    path('add_category/', add_category, name='add_category'),
    path('product/update/<int:pk>/', update_Product, name='update_product'), 
    path('list/', product_list, name='product_list'), 
    path('product/delete/<int:pk>/', deleteProduct, name='delete_product'), 
    path('rent_product/', rent_product, name='rent_product'),
      

]