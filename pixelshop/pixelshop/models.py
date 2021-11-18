"""Models module."""
import os
from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from djmoney.models.fields import MoneyField


# Create your models here.
class User(models.Model):
    """User class."""

    login = models.CharField(max_length=45)
    passwd = models.CharField(max_length=45)
    email = models.EmailField()


class PixelArt(models.Model):
    """PixelArt class."""

    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    file = models.FilePathField(path=os.path.join(settings.LOCAL_FILE_DIR, 'images'))
    price = MoneyField(
        verbose_name='Cena',
        max_digits=14,
        decimal_places=2,
        default_currency='PLN',
        default=0.0,
    )
    certificate_id = models.CharField(max_length=128)


class Order(models.Model):
    """Order class."""
    NEW = 'new'
    IN_PROGRESS = 'in_progres'
    PAYMENT_RECEIVED = 'payment_received'
    PAYMENT_FAILED = 'payment_failed'
    COMPLETED = 'completed'
    CANCELED = 'canceled'
    STATUS_CHOICES = [
        (NEW, 'new'),
        (IN_PROGRESS, 'in progress'),
        (PAYMENT_RECEIVED, 'payment received'),
        (PAYMENT_FAILED, 'payment failed'),
        (COMPLETED, 'completed'),
        (CANCELED, 'canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pixelart = models.ForeignKey(PixelArt, on_delete=models.PROTECT)
    date_purchased = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEW,
    )