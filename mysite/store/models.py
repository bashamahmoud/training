from django.db import models


class User(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)

    class Meta:
        abstract = True


class Customer(User):
    credit_card = models.CharField(max_length=60)


class Admin(User):
    pass


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField()
    in_inventory = models.IntegerField()


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')
