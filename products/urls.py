from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/', views.get_product_by_id),
    path('products/', views.get_all_products),
    path('products/<int:product_id>/update/', views.update_product),
    path('products/<int:product_id>/delete/', views.delete_product),
    path('products/create/', views.create_product),
]
