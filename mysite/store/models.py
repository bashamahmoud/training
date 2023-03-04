from django.db import models


# user
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
