from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    total = models.FloatField()
    products = models.TextField()   # ADD THIS LINE
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name