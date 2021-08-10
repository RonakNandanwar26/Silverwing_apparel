from django.urls import path
from .views import products,category,product_list,singleproduct,my_products,update_products

app_name = 'Products'

urlpatterns = [
    path('product_form/',products,name='products'),
    path('category_form/',category,name='category'),
    path('list/',product_list,name='product_list'),
    path('singleproduct/<int:pk>/',singleproduct,name='singleproduct'),
    path('my_products/',my_products,name='my_products'),
    path('update_products/<int:pk>/',update_products,name='update_products')
]

