from django.urls import path
from . import views

urlpatterns = [
    # Главная страница — список всех товаров
    path('', views.product_list, name='product_list'),

    # Страница товара по его ID
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
