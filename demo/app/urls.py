from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category-detail/<int:id>/', views.category_detail, name='category_detail'),
    path('product-detail/<int:id>/', views.product_detail, name='product_detail'),

  
]
