from django.db import models

class Product(models.Model):
    # Название товара
    name = models.CharField(max_length=255, verbose_name="Название")

    # Подробное описание товара
    description = models.TextField(verbose_name="Описание")

    # Цена товара (до 99999999.99)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    # Изображение товара, загружается в папку media/products/
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")

    # Дата и время добавления товара
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name
