from django.db import models
from django.contrib.auth.models import User


class Firm(models.Model):

    name = models.CharField(max_length=120)

    def __str__(self):

        return f'{self.name}'


class Sneakers(models.Model):

    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to='images')
    obj_3d = models.FileField(upload_to='files')
    price = models.PositiveIntegerField(default=999)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.title} {self.firm} {self.price}'


class CartItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.sneakers}'


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(CartItem, through="OrderCart")
    price = models.PositiveIntegerField(default=0)


class OrderCart(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartItem, on_delete=models.CASCADE)
