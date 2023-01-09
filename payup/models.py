"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
import uuid
from django.contrib.auth.models import User
# Internal
from products.models import Prod
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Order(models.Model):
    order_number = models.CharField(
        max_length=12,
        null=False,
        editable=False
        )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
        )
    email = models.EmailField(
        max_length=80,
        null=False,
        blank=False
        )
    phone_number = models.CharField(
        max_length=11,
        null=False,
        blank=False
        )
    canton = models.CharField(
        max_length=40,
        null=False,
        blank=False)
    city = models.CharField(
        max_length=40,
        null=False,
        blank=False
        )
    postcode = models.CharField(
        max_length=6,
        null=True,
        blank=True
        )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
        )
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    date = models.DateTimeField(
        auto_now_add=True
        )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
        )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    def _order_nbr_gen(self):
            """
            Generate a random and unique order number
            """
            return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total function
        """
        self.order_total = self.lineitems.aggregate(Sum('prods_total'))['prods_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._order_nbr_gen()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrdProd(models.Model):
    """
    Products in the order
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='prodsorder'
        )
    product = models.ForeignKey(
        Prod,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
        )
    prods_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
        )
    def save(self, *args, **kwargs):
        """
        Update the order total.
        """
        if self.scount > 0:
            self.prods_total = self.product.price * self.quantity * self.scount
        else:
            self.prods_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
