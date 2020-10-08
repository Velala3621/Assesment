from django.db import models
from django.urls import reverse
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image=models.FileField(upload_to='images/',default=None, null=True , blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('product-update', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.title} {self.description} "


class Productitem(models.Model):
    profile = models.ForeignKey(Product, on_delete=models.PROTECT)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2,default='0')

    def __str__(self):
        return self.item_name
