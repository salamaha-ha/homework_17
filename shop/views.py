from django.shortcuts import render, get_object_or_404
from .models import Product

# Представление для отображения списка всех товаров
def product_list(request):
    # Получаем все товары из базы, отсортированные по дате добавления
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'shop/product_list.html', {'products': products})

# Представление для отображения информации о конкретном товаре
def product_detail(request, product_id):
    # Пытаемся найти товар по id, если не найден — будет 404
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})
