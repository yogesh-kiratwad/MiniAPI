from django.db import models

# Create your models here.
class FBrand(models.Model):
    fbrand = models.CharField(max_length=100)

    def __str__(self):
        return self.fbrand

class FCategory(models.Model):
    fcategory = models.CharField(max_length=100)

    def __str__(self):
        return self.fcategory
        

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(FBrand, on_delete=models.CASCADE, related_name='pbrand')
    category = models.ForeignKey(FCategory, on_delete=models.CASCADE, related_name='pcategory')
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.brand
    
    
