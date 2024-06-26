from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):

    STATUS_CHOICES =[
        ('Available','Available'),
        ('On sale', 'On sale'),
        ('Out of stock', 'Out of stock')
    ]

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[self.pk])
    
    def update_status(self, *args, **kwargs):
        if self.stock == 0:
            self.status = 'Out of stock'
        else:
            self.status = 'Available'
        super().save(*args, **kwargs)


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('On cart', 'On cart'),
        ('To Pay', 'To Pay'),
        ('To Ship', 'To Ship'),
        ('To Receive', 'To Receive'),
        ('Delivered', 'Delivered'),
    ]

    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)