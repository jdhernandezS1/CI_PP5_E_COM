"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Internal
from .models import OrdProd
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@receiver(post_save, sender=OrdProd)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on product update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrdProd)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
