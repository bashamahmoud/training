from django.db import models


class User(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Customer(User):
    credit_card = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Admin(User):
    pass

    def __str__(self):
        return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=60)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10)
#     inventory = models.IntegerField(max_digits=10)
#
#     def __str__(self):
#         return self.name
#
#
# class Cart(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#
#     def __str__(self):
#         return f"{self.customer.username}'s cart"
