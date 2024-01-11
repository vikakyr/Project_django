from django.db import models

# Create your models here.

class Category(models.Model):
    HELMET = 'Helmet'
    SKIS = 'Skis'
    POLES = 'Poles'
    BOOTS = 'Boots'

    CATEGORY_CHOICES = [
        (HELMET, 'Helmet'),
        (SKIS, 'Skis'),
        (POLES, 'Poles'),
        (BOOTS, 'Boots'),
    ]

    def __str__(self):
        return self.name

    name = models.CharField(max_length=15, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Level(models.Model):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'

    LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    def __str__(self):
        return self.name

    name = models.CharField(max_length=15, choices=LEVEL_CHOICES)

    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"


class Products(models.Model):
    name = models.CharField(max_length=100)
    description =  models.TextField(blank=True)
    price =  models.DecimalField(max_digits=999, decimal_places=2)


    # przypisanie produktu do kategorii oraz poziomu
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    level = models.ForeignKey(Level,on_delete=models.CASCADE, null=True)


    # wyświetlanie właśniwej nazwy
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

# from django.db import models
# from django.conf import settings

# class ReservedProduct(models.Model):
#     product_id = models.IntegerField()
#     category = models.CharField(max_length=255)
#     selected_size = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.product_id} - {self.category} - {self.selected_size} - {self.price} - {self.date} - {self.user.username}'

    
# class ReservedProductt(models.Model):
#     product_id = models.IntegerField()
#     category = models.CharField(max_length=255)
#     selected_size = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()
#     username = models.CharField(max_length=255)

#     def __str__(self):
#         return f'{self.product_id} - {self.category} - {self.selected_size} - {self.price} - {self.date} - {self.username}'


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class ReservedProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    selected_size = models.CharField(max_length=50) 
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.date} - {self.selected_size} - {self.category}"

    class Meta:
        verbose_name = "Reserved Product"
        verbose_name_plural = "Reserved Products"