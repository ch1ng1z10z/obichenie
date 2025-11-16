from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Катерогия"
        verbose_name_plural = 'Катерогии'

    def __str__(self):
        return self.name    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    image = models.ImageField(upload_to='products/%Y%m%d')