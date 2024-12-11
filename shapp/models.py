from django.db import models


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

    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.sneakers}'
