from django.urls import path 

from .views import ProductList , ProductDetail , add_review

app_name = 'product'

urlpatterns = [
    path('',ProductList.as_view(),name='product_list'),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),
    path('<slug:slug>/add-review',add_review,name='add_review'),
]