from django.db import models
from .category import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_All_Products():
        return Product.objects.all()

    @staticmethod
    def get_Products_by_categoryId(categoryID):
        if categoryID:
            return Product.objects.filter(
                category=categoryID
            )

        else:
            return Product.get_All_Products()
