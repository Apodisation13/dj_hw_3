from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение')
    release_date = models.DateTimeField(verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(verbose_name='lte', default=True)
    slug = models.SlugField(unique=True)
