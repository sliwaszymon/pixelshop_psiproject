"""Models module."""
# Standard Library
import hashlib
import os

# Django
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

# 3rd-party
from djmoney.models.fields import MoneyField


class User(AbstractUser):
    """User class."""

    class Meta:
        """Meta class."""

        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        """Str magic method for User class."""
        return f'{self.email} {self.username}'

    def get_absolute_url(self):
        """Get_absolute_url method for User class."""
        return reverse('user-detail', kwargs={'pk': self.pk})


class PixelArt(models.Model):
    """PixelArt class."""

    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    file = models.FilePathField(
        path=os.path.join(
            settings.LOCAL_FILE_DIR,
            'static\images',
            ),
        )
    price = MoneyField(
        verbose_name='Cena',
        max_digits=14,
        decimal_places=2,
        default_currency='PLN',
        default=0.0,
        )
    certificate_id = models.CharField(max_length=128)

    class Meta:
        """Meta class."""

        verbose_name = _('pixelart')
        verbose_name_plural = _('pixelarts')

    def __str__(self):
        """Str magic method for PixelArt class."""
        return f'{self.title} {self.price}'

    def save(self, *args, **kwargs):
        """Save method for PixelArt class."""
        certid = hashlib.sha256(b'{self.title}{self.desc}').hexdigest()
        self.certificate_id = certid
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Get_absolute_url method for PixelArt class."""
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
    date_purchased = models.DateTimeField(default=now, editable=False)
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default='new',
    )

    class Meta:
        """Meta class."""

        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        """Str magic method for Order class."""
        return f'{self.pixelart} - {self.user} - {self.date_purchased} - {self.status}'

    def get_absolute_url(self):
        """Get_absolute_url method for Order class."""
        return reverse('order-detail', kwargs={'pk': self.pk})
