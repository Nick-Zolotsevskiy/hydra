from django.urls import path
from hydra_shop import views

urlpatterns = [
    path('', views.index),

    path('categories/', views.categories_list),
    path('categories/<int:category_id>/', views.products_list),
    path('products/<int:product_id>/', views.product_info),
]
