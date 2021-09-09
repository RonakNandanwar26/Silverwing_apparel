from django.urls import path
from .views import (products,
                    category,
                    product_list,
                    singleproduct,
                    update_products,
                    my_products,
                    delete_product,
                    ratings,
                    search,
                    winter,summer,Male,Female)

app_name = 'Products'

urlpatterns = [
    path('product_form/',products,name='products'),
    path('category_form/',category,name='category'),
    path('list/',product_list,name='product_list'),
    path('singleproduct/<int:pk>/',singleproduct,name='singleproduct'),
    path('my_products/',my_products,name='my_products'),
    path('update_products/<int:pk>/',update_products,name='update_products'),
    path('delete_product/<int:pk>/',delete_product,name='delete_product'),
    path('ratings/<int:pk>/',ratings,name='ratings'),
    path('search/',search,name='search'),
    path('winter/',winter,name='winter'),
    path('summer/',summer,name='summer'),
    path('Male/',Male,name='Male'),
    path('Female/',Female,name='Female'),
]

