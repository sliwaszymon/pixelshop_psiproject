"""Models module."""
import os
import hashlib
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from django.urls import reverse
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    """User class."""

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.email} {self.username}"

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

class PixelArt(models.Model):
    """PixelArt class."""

    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    file = models.FilePathField(path=os.path.join(settings.LOCAL_FILE_DIR, 'static\images'))
    price = MoneyField(
        verbose_name='Cena',
        max_digits=14,
        decimal_places=2,
        default_currency='PLN',
        default=0.0,
    )
    certificate_id = models.CharField(max_length=128)

    class Meta:
        verbose_name = _('pixelart')
        verbose_name_plural = _('pixelarts')

    def __str__(self):
        return f"{self.title} {self.price}"

    def save(self, *args, **kwargs):
        certid = hashlib.sha256(b'{self.title}{self.desc}').hexdigest()
        self.certificate_id = certid
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pixelart-detail', kwargs={'pk': self.pk})


class OrderStatus(models.TextChoices):
    """OrderStatus choices class."""

    NEW = 'new'
    IN_PROGRESS = 'in_progres'
    PAYMENT_RECEIVED = 'payment_received'
    PAYMENT_FAILED = 'payment_failed'
    COMPLETED = 'completed'
    CANCELED = 'canceled'


class Order(models.Model):
    """Order class."""

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pixelart = models.ForeignKey(PixelArt, on_delete=models.PROTECT)
    date_purchased = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default='new',
    )

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
    

    def __str__(self):
        return f"{self.pixelart} - {self.user} - {self.date_purchased} - {self.status}"

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})
